import pydirectinput
import time

# Coordenadas para hacer clic
clic_x = 1702
clic_y = 697

#clic_x = 1066
#clic_y = 701

try:
    while True:
        # Hacemos clic en las coordenadas especificadas
        #time.sleep(1.3)
        pydirectinput.click(clic_x, clic_y)
        #pydirectinput.press('4')
        print(f'Se ha hecho clic en las coordenadas: X={clic_x}, Y={clic_y}')

        # Esperamos 3 segundos antes del próximo clic
        #time.sleep(3.1)
        
        time.sleep(3)
except KeyboardInterrupt:
    print("¡Saliendo del programa!")