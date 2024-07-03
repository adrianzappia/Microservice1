import pydirectinput
import time




# Título de la ventana del programa de Windows
import pygetwindow as gw



window_title = "NIGHT CROWS(1)"

# Ruta de la plantilla del objeto que deseas detectar
#template_path = 'btn_todos.png'

# Obtener la ventana del programa de Windows por su título
window = gw.getWindowsWithTitle(window_title)[0]
left, top, width, height = window.left, window.top, window.width, window.height

print("Posición izquierda:", left)
print("Posición superior:", top)
print("Ancho:", width)
print("Altura:", height)



try:
    while True:
        #menu
        pydirectinput.click(left+960,top+50)
        time.sleep(1)
        #misiones
        pydirectinput.click(left+800,top+153)
        time.sleep(1)
        
        #diarias
        pydirectinput.click(left+282,top+91)
        time.sleep(1)
        
        
        #misiones bastium
        pydirectinput.click(left+48,top+159)
        time.sleep(1)
        

        #recorro las misiones de bastium
        for i in range(8):  # Realiza 6 clics
            pydirectinput.click(left + 230, top + 200 + i*30)
            time.sleep(1)
            pydirectinput.click(left + 780, top + 582)
            time.sleep(1)
        
        
        #misiones celano
        pydirectinput.click(left+48,top+189)
        time.sleep(1)
        
        #recorro las misiones de celano
        for i in range(6):  # Realiza 6 clics
            pydirectinput.click(left + 230, top + 200 + i*30)
            time.sleep(1)
            pydirectinput.click(left + 780, top + 582)
            time.sleep(1)
        
        #una vez que marco todas las que necesito voy
        #a la primera y le doy automatico
        #misiones bastium
        pydirectinput.click(left+48,top+159)
        time.sleep(1)
        for i in range(1):  # Realiza 1 clics
            pydirectinput.click(left + 230, top + 200 + i*30)
            time.sleep(1)
        pydirectinput.click(left + 780, top + 582)
        time.sleep(1)
        pydirectinput.press('y')
        break
        
        
        
        
        #menu
        #pydirectinput.click(left+960,top+50)
        #time.sleep(1)
        
        
            
except KeyboardInterrupt:
    print("¡Saliendo del programa!")