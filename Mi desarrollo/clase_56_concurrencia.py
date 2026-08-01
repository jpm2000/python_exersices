from concurrent.futures import thread
import threading
import time

# Aplicando la concurrencia


# Funcion que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f"Procesando solicitud {request_id}")
    time.sleep(3)
    print(f"Solicitud {request_id} completa")


threads = []

for i in range(3):
    # Crear un nuevo hilo que ejecuta la función
    # i es igual al request_id, le pongo una coma para que lo tome como un iterable
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    # Va a asegurar a que el programa espere a que cada hilo termine
    thread.join()

print("Todas las solicitudes fueron completadas")
