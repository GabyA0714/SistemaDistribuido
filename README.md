PFO 3: Sistema Distribuido (Cliente-Servidor)

Este repositorio contiene la resolución de la Práctica Formativa Obligatoria 3. El objetivo del proyecto es diseñar una arquitectura distribuida y simular un entorno de procesamiento asíncrono, utilizando comunicación por Sockets TCP nativos en Python y manejo de concurrencia.

Arquitectura del Sistema (Diseño)
El diseño topológico contempla:
* Clientes (Web y Móviles) conectándose a través de un Balanceador de Carga (Nginx/HAProxy).
* Un pool de Servidores Workers para procesamiento concurrente.
* Comunicación asíncrona mediante una Cola de Mensajes (RabbitMQ).
* Persistencia de datos distribuidos (PostgreSQL para datos estructurados y S3 para almacenamiento de objetos).

*(Diagrama del Sistema Distribuido.png)*

(Diagrama del Sitema Distribuido.png)
<img width="1081" height="622" alt="Diagrama del Sistema Distribuido drawio" src="https://github.com/user-attachments/assets/af1d455c-3dee-494a-94f8-bb7548420bc0" />

Alcance de la Implementación (Código)
Para esta fase del proyecto, se implementó el núcleo de la comunicación distribuida:
* **Lenguaje:** Python 3
* **Librerías estándar:** `socket`, `concurrent.futures`
* **Mecanismo:** El servidor implementa nativamente un pool de hilos (`ThreadPoolExecutor`) para distribuir y procesar las peticiones de los clientes de forma concurrente, simulando el comportamiento de los workers con un manejo robusto de excepciones y desconexiones.

Instrucciones de Ejecución
Para validar la comunicación entre los nodos mediante sockets, se requieren dos instancias de terminal ejecutándose en paralelo.

1. **Iniciar el Servidor (Worker Pool):** Ejecutar en la primera terminal para levantar el servidor en el puerto 65432 y habilitar el pool de 5 hilos.
   ```bash
   python servidor.py
2. **Iniciar el Cliente: Ejecutar en la segunda terminal para enviar la carga de trabajo.
    ```bash
   python cliente.py

    Evidencia de Ejecución
A continuación se detalla la salida de consola (logs) comprobando la correcta conexión TCP, el procesamiento asíncrono y el manejo seguro de conexiones:

Terminal 1 (Servidor):Gabriela@DESKTOP-SU7BE1A MINGW64 ~/Desktop/SistemaDistribuido (main)
$ python servidor.py
=== Servidor distribuido escuchando en 127.0.0.1:65432 ===
=== Pool de hilos inicializado con 5 workers ===

[+] Conexión establecida desde ('127.0.0.1', 55287)
[*] Tarea recibida de ('127.0.0.1', 55287): 'Generar reporte de procesamiento mensual'
[-] Conexión cerrada con ('127.0.0.1', 55287)

Terminal 2 (Cliente):

Gabriela@DESKTOP-SU7BE1A MINGW64 ~/Desktop/SistemaDistribuido (main)
$ python cliente.py
Conectando al servidor 127.0.0.1:65432...
Enviando tarea: 'Generar reporte de procesamiento mensual'
Respuesta del servidor: Tarea 'Generar reporte de procesamiento mensual' procesada exitosamente por el worker.
Conexión finalizada.
