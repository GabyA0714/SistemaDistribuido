import socket

HOST = '127.0.0.1'
PORT = 65432

def enviar_tarea(tarea):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        cliente.connect((HOST, PORT))
        
        cliente.sendall(tarea.encode('utf-8'))
        
        datos_recibidos = cliente.recv(1024)
        print(f"Respuesta del servidor: {datos_recibidos.decode('utf-8')}")
        
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor. Verifique que esté en ejecución.")
    finally:
        cliente.close()

if __name__ == "__main__":
    tarea_asignada = "Generar reporte de procesamiento"
    print(f"Enviando tarea: {tarea_asignada}")
    enviar_tarea(tarea_asignada)