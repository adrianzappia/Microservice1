import pydirectinput
import time

# Coordenadas para hacer clic
clic_x = 1702
clic_y = 697

#clic_x = 1066
#clic_y = 701

try:
    while True:
        pydirectinput.press('4')
        time.sleep(1)
except KeyboardInterrupt:
    print("¡Saliendo del programa!")