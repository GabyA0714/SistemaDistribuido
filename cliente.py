import socket

HOST = '127.0.0.1'
PORT = 65432

def enviar_tarea(tarea):
    # Usamos timeout por si el servidor se cuelga y no responde
    socket.setdefaulttimeout(5.0) 
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"Conectando al servidor {HOST}:{PORT}...")
        cliente.connect((HOST, PORT))
        
        # Enviamos la tarea
        print(f"Enviando tarea: '{tarea}'")
        cliente.sendall(tarea.encode('utf-8'))
        
        # Esperamos respuesta
        datos_recibidos = cliente.recv(1024)
        
        if datos_recibidos:
            print(f"Respuesta del servidor: {datos_recibidos.decode('utf-8')}")
        else:
            print("El servidor cerró la conexión sin enviar respuesta.")
            
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor. Verifique que esté en ejecución.")
    except socket.timeout:
        print("Error: El servidor tardó demasiado en responder (Timeout).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        cliente.close()
        print("Conexión finalizada.")

if __name__ == "__main__":
    tarea_asignada = "Generar reporte de procesamiento mensual"
    enviar_tarea(tarea_asignada)