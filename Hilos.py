import threading #importar hilos

def print_function(): # funcion
    print("El hilo está corriendo") # imprimo
t = threading.Thread(target=print_function)

t.start() # que comience

t.join() # para poder tener multihilos

#----------------------------------------

# Definimos constantes de colores en ANSI para cambiar el color de texto en la consola
verde = "\033[1;32m"    # Color verde claro para texto
amarillo = "\033[1;33m" # Color amarillo para texto
azul = "\033[1;36m"     # Color azul claro para texto
gris = "\033[0;37m"     # Color gris (o reset) para volver al color de texto original

# Importamos módulos necesarios
from datetime import datetime # Módulo para manejar fechas y horas
import time                    # Módulo para agregar retrasos de tiempo en segundos
import threading               # Módulo para trabajar con hilos (concurrencia)

# Función que muestra la hora en un color específico
def mostrar_hora(color):
    """
    Muestra la hora actual en la consola en el color especificado,
    repitiendo la impresión 100 veces, con un segundo de espera entre cada impresión.

    Parámetros:
    color (str): Cadena ANSI que define el color de texto para la salida
    """
    for i in range(100):  # Iteramos 100 veces
        # Capturamos la hora actual en formato 'hora:minuto:segundo.milisegundo'
        hora = datetime.now().strftime("%H:%M:%S.%f")
        # Imprimimos el número de iteración, la hora, y el color especificado
        print(f"{color}#{i} {hora}{gris}")
        # Esperamos 1 segundo antes de la siguiente iteración
        time.sleep(1)

# Bloque principal de ejecución del programa
if __name__ == "__main__":
    # Guardamos el tiempo inicial para medir la duración total de la ejecución
    inicio = datetime.now()
    
    # Ejecutamos la función mostrar_hora en el color verde y luego en amarillo
    # Sin embargo, esta ejecución es secuencial, lo que significa que verde y luego amarillo.
    # Esto es solo un ejemplo de ejecución, no es multihilo.
    mostrar_hora(verde)
    mostrar_hora(amarillo)
    
    # Creamos dos hilos, uno para cada color (verde y amarillo) y asignamos
    # la función mostrar_hora a cada hilo, pasándole el color correspondiente como argumento
    h1 = threading.Thread(target=mostrar_hora, args=(verde,))
    h2 = threading.Thread(target=mostrar_hora, args=(amarillo,))
    
    # Iniciamos la ejecución de ambos hilos en paralelo
    h1.start()
    h2.start()
    
    # Usamos .join() en cada hilo para hacer que el programa principal
    # espere hasta que ambos hilos hayan terminado su ejecución
    h1.join()
    h2.join()
    
    # Imprimimos una línea vacía para separar visualmente la salida de la duración total
    print()
    # Calculamos el tiempo total que ha pasado desde el inicio hasta el final de los hilos
    # y mostramos el resultado en segundos
    print(f"Finalizado en {(datetime.now() - inicio).total_seconds()} segundos")  

 