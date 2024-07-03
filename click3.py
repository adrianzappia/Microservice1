import pydirectinput
import time

try:
    while True:
        # Obtenemos las coordenadas del mouse
        x, y = pydirectinput.position()

        # Imprimimos las coordenadas del mouse
        print(f'Coordenadas del mouse: X={x}, Y={y}')
        time.sleep(1)

except KeyboardInterrupt:
    print("¡Saliendo del programa!")