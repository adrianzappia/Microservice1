import pydirectinput
import time

# Coordenadas para hacer clic
clic_x = 1522
clic_y = 738

#clic_x = 1066
#clic_y = 701
cont =0
try:
    while True:
        if cont==500:
            pydirectinput.click(1588,213)
            time.sleep(0.2)
            pydirectinput.click(730,265)
            time.sleep(0.3)
            pydirectinput.click(728,413)
            time.sleep(0.8)
            pydirectinput.click(1372,509)
            time.sleep(0.8)
            pydirectinput.click(1312,742)
            time.sleep(0.2)
            cont=0
        else:
     
    
    
            # Hacemos clic en las coordenadas especificadas
            #time.sleep(1.3)
            #pydirectinput.click(clic_x, clic_y)
            #pydirectinput.press('4')
            print(f'Se ha hecho clic en las coordenadas: X={clic_x}, Y={clic_y}')

            # Esperamos 3 segundos antes del próximo clic
            #time.sleep(3.1)
            time.sleep(0.1)
            pydirectinput.click(1150,341)
            time.sleep(0.1)
            pydirectinput.click(1150,341)
            time.sleep(0.1)
            pydirectinput.click(1126,609)
            #pydirectinput.click(1122,624)
            #pydirectinput.click(1125,602)
            #pydirectinput.click(1128,623)
            time.sleep(0.1)
            pydirectinput.click(1180,534)
            time.sleep(0.1)
            pydirectinput.click(1242,314)
            time.sleep(0.1)
            pydirectinput.click(713,324)
            time.sleep(0.5)
        cont=cont+1
        print(f'coord:{cont}')
except KeyboardInterrupt:
    print("¡Saliendo del programa!")
    
    
    