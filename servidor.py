import socket
import concurrent.futures

HOST = '127.0.0.1'
PORT = 65432
MAX_WORKERS = 5

def procesar_tarea_worker(conexion, direccion):
    try:
        print(f"Conexión establecida desde {direccion}")
        
        datos = conexion.recv(1024)
        if not datos:
            return

        mensaje_recibido = datos.decode('utf-8')
        print(f"Tarea recibida de {direccion}: {mensaje_recibido}")
        
        resultado = f"Tarea '{mensaje_recibido}' procesada correctamente por el worker."
        
        conexion.sendall(resultado.encode('utf-8'))
    except Exception as e:
        print(f"Error procesando tarea de {direccion}: {e}")
    finally:
        conexion.close()
        print(f"Conexión cerrada con {direccion}")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    
    print(f"Servidor distribuido escuchando en {HOST}:{PORT}")
    print(f"Pool de hilos inicializado con {MAX_WORKERS} workers.")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        try:
            while True:
                conexion, direccion = servidor.accept()
                executor.submit(procesar_tarea_worker, conexion, direccion)
        except KeyboardInterrupt:
            print("\nApagando servidor...")
        finally:
            servidor.close()

if __name__ == "__main__":
    iniciar_servidor()