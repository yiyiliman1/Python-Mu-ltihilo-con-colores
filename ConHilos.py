# CON HILOS (WITH THREADS)
import threading          # Importa el módulo 'threading' para crear y manejar hilos (threads)
from datetime import datetime # Importa 'datetime' para manejar fechas y horas
import time               # Importa 'time' para manejar retrasos temporales en segundos

# COLORES (Use el “reset” al final)
verde = "\033[1;32m"      # Código ANSI para texto en color verde claro
amarillo = "\033[1;33m"   # Código ANSI para texto en color amarillo
azul = "\033[1;36m"       # Código ANSI para texto en color cyan (azul claro)
gris = "\033[0;37m"      # Código ANSI para restablecer el color al original después de imprimir
naranja = "\033[1;91m"          # Naranja claro
rosa = "\033[1;95m"             # Rosa claro
verde_lima = "\033[1;92m"       # Verde lima
azul_cielo = "\033[1;94m"       # Azul cielo
violeta = "\033[1;95m"          # Violeta claro
marron = "\033[0;33m"           # Marrón (oscuro, similar a amarillo oscuro)
verde_oliva = "\033[0;32m"      # Verde oliva
azul_marino = "\033[0;34m"      # Azul marino (oscuro)
gris_claro = "\033[0;90m"       # Gris claro
rosa_fuerte = "\033[1;35m"      # Rosa fuerte (similar a fucsia)

# FUNCIÓN que muestra la hora (se ejecutará en cada hilo con diferente color)
def mostrar_hora(color):
    """
    Imprime la hora actual en el color especificado, repitiendo la impresión 100 veces.
    
    Parámetros:
    color (str): Cadena ANSI que define el color del texto en la consola.
    """
    for i in range(100):  # Bucle que se repite 100 veces
        # Captura la hora actual en el formato 'horas:minutos:segundos.milisegundos'
        hora = datetime.now().strftime("%H:%M:%S.%f")
        # Imprime el número de iteración, la hora actual y el color
        print(f"{color} #{i} {hora} {gris}")
        # Pausa la ejecución durante 1 segundo antes de la próxima iteración
        time.sleep(1)

# MAIN (Hacemos que cada hilo muestre la hora en un color distinto)
# Creamos 3 hilos, uno para cada color: verde, amarillo y cyan
# Cada hilo ejecutará la función mostrar_hora con un color diferente

# Creamos el hilo h1 que ejecutará 'mostrar_hora' con el color verde
h1 = threading.Thread(target=mostrar_hora, args=(verde,))
# Creamos el hilo h2 que ejecutará 'mostrar_hora' con el color amarillo
h2 = threading.Thread(target=mostrar_hora, args=(amarillo,))
# Creamos el hilo h3 que ejecutará 'mostrar_hora' con el color cyan
h3 = threading.Thread(target=mostrar_hora, args=(azul,))
h4 = threading.Thread(target=mostrar_hora, args=(naranja,))
h5 = threading.Thread(target=mostrar_hora, args=(rosa,))
h6 = threading.Thread(target=mostrar_hora, args=(verde_lima,))
h7 = threading.Thread(target=mostrar_hora, args=(azul_cielo,))
h8 = threading.Thread(target=mostrar_hora, args=(violeta,))
h9 = threading.Thread(target=mostrar_hora, args=(marron,))
h10 = threading.Thread(target=mostrar_hora, args=(verde_oliva,))
h11 = threading.Thread(target=mostrar_hora, args=(azul_marino,))
h12 = threading.Thread(target=mostrar_hora, args=(gris_claro,))
h13 = threading.Thread(target=mostrar_hora, args=(rosa_fuerte,))
h14 = threading.Thread(target=mostrar_hora, args=(verde,))
h15 = threading.Thread(target=mostrar_hora, args=(amarillo,))
h16 = threading.Thread(target=mostrar_hora, args=(azul,))
h17 = threading.Thread(target=mostrar_hora, args=(naranja,))
h18 = threading.Thread(target=mostrar_hora, args=(rosa,))
h19 = threading.Thread(target=mostrar_hora, args=(verde_lima,))
h20 = threading.Thread(target=mostrar_hora, args=(azul_cielo,))


# INICIAMOS LOS HILOS
# Comienza la ejecución de cada hilo en paralelo
h1.start()
h2.start()
h3.start()
h4.start()
h5.start()
h6.start()
h7.start()
h8.start()
h9.start()
h10.start()
h11.start()
h12.start()
h13.start()
h14.start()
h15.start()
h16.start()
h17.start()
h18.start()
h19.start()
h20.start()

# OBLIGAMOS A QUE LOS HILOS FINALICEN SU EJECUCIÓN ANTES DE CONTINUAR CON EL PROGRAMA
# Usamos join() para esperar a que cada hilo termine antes de continuar
h1.join()
h2.join()
h3.join()
h4.join()
h5.join()
h6.join()
h7.join()
h8.join()
h9.join()
h10.join()
h11.join()
h12.join()
h13.join()
h14.join()
h15.join()
h16.join()
h17.join()
h18.join()
h19.join()
h20.join()

# MOSTRAMOS LOS SEGUNDOS QUE HA TARDADO
# Guardamos el tiempo de inicio para medir la duración de ejecución
inicio = datetime.now()
print()  # Imprime una línea en blanco para separar visualmente la salida de tiempo
# Calculamos el tiempo total en segundos desde el inicio y mostramos el tiempo transcurrido
print(f"Finalizado en {(datetime.now() - inicio).total_seconds()} segundos")