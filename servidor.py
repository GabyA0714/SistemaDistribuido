import socket
import concurrent.futures

HOST = '127.0.0.1'
PORT = 65432
MAX_WORKERS = 5

def procesar_tarea_worker(conexion, direccion):
    try:
        print(f"[+] Conexión establecida desde {direccion}")
        
        datos = conexion.recv(1024)
        
        # Manejo de mensajes vacíos
        if not datos:
            print(f"[-] Cliente {direccion} envió un mensaje vacío o cerró la conexión.")
            return

        mensaje_recibido = datos.decode('utf-8').strip()
        print(f"[*] Tarea recibida de {direccion}: '{mensaje_recibido}'")
        
        # Procesamiento simulado
        resultado = f"Tarea '{mensaje_recibido}' procesada exitosamente por el worker."
        conexion.sendall(resultado.encode('utf-8'))
        
    except ConnectionResetError:
        # Manejo de desconexión abrupta (ej: se cerró la terminal del cliente de golpe)
        print(f"[!] Error: El cliente {direccion} se desconectó abruptamente.")
    except Exception as e:
        print(f"[!] Error inesperado procesando tarea de {direccion}: {e}")
    finally:
        conexion.close()
        print(f"[-] Conexión cerrada con {direccion}\n")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Esta línea permite reiniciar el servidor sin el error "Address already in use"
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print(f"=== Servidor distribuido escuchando en {HOST}:{PORT} ===")
        print(f"=== Pool de hilos inicializado con {MAX_WORKERS} workers ===\n")

        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            while True:
                conexion, direccion = servidor.accept()
                executor.submit(procesar_tarea_worker, conexion, direccion)
                
    except KeyboardInterrupt:
        print("\n[!] Apagando servidor de forma segura...")
    finally:
        servidor.close()

if __name__ == "__main__":
    iniciar_servidor()