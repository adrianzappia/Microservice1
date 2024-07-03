import pydirectinput
import time



tiempo_curar=0;
try:
    while True:
        if (tiempo_curar==4):
            pydirectinput.press('f1')
            time.sleep(0.1)
            pydirectinput.press('4')
            time.sleep(0.1)
            pydirectinput.press('f1')
            time.sleep(0.1)
            tiempo_curar=0
        else:
            pydirectinput.press('f')
            time.sleep(0.1)
        
        pydirectinput.press('r')
        time.sleep(0.1)    
                    
        #if (tiempo==3):
        #        pydirectinput.press('r')
        #        pydirectinput.press('f')       
        tiempo_curar=tiempo_curar+0.5
        time.sleep(0.5)
except KeyboardInterrupt:
    print("¡Saliendo del programa!")