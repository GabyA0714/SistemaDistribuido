PFO 3: Sistema Distribuido (Cliente-Servidor)

Este repositorio contiene la resolución de la Práctica Formativa Obligatoria 3. El objetivo del proyecto es implementar una arquitectura distribuida simulando un entorno de procesamiento asíncrono y balanceo de carga, utilizando comunicación por Sockets TCP nativos en Python.

Arquitectura del Sistema

El diseño topológico contempla:
* Clientes (Web y Móviles) conectándose a través de un Balanceador de Carga (Nginx/HAProxy).
* Un pool de Servidores Workers para procesamiento concurrente.
* Comunicación asíncrona mediante una Cola de Mensajes (RabbitMQ).
* Persistencia de datos distribuidos (PostgreSQL para datos estructurados y S3 para almacenamiento de objetos).

(Diagrama del Sitema Distribuido.png)
<img width="1081" height="622" alt="Diagrama del Sistema Distribuido drawio" src="https://github.com/user-attachments/assets/af1d455c-3dee-494a-94f8-bb7548420bc0" />


Tecnologías Utilizadas
* Lenguaje: Python 3
* Librerías estándar: `socket`, `concurrent.futures`

Instrucciones de Ejecución

Para validar la comunicación entre los nodos mediante sockets, se requieren dos instancias de terminal ejecutándose en paralelo.

1. Iniciar el Servidor (Worker Pool):
Ejecutar en la primera terminal para levantar el servidor en el puerto 65432 y habilitar el pool de 5 hilos.
```bash
python servidor.py

Evidencia de Ejecución

A continuación se detalla la salida de consola (logs) comprobando la correcta conexión TCP y el procesamiento asíncrono entre ambos nodos:

**Terminal 1 (Servidor):**
```text
Servidor distribuido escuchando en 127.0.0.1:65432
Pool de hilos inicializado con 5 workers.
Conexión establecida desde ('127.0.0.1', 54162)
Tarea recibida de ('127.0.0.1', 54162): Generar reporte de procesamiento
Conexión cerrada con ('127.0.0.1', 54162)
Terminal 2 (Cliente):
Enviando tarea: Generar reporte de procesamiento
Respuesta del servidor: Tarea 'Generar reporte de procesamiento' procesada correctamente por el worker.
