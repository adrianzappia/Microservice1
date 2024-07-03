import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import time
import pydirectinput
import datetime

# Función para detectar el objeto y obtener las coordenadas de coincidencia
def detect_object(window, template_path,threshold):
    center_x=0
    center_y=0
    # Obtener las dimensiones de la ventana
    left, top, width, height = window.left, window.top, window.width, window.height

    # Capturar la pantalla dentro de la ventana del programa
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Cargar la plantilla del objeto que deseas detectar
    template = cv2.imread(template_path, 0)

    # Obtener las dimensiones de la plantilla
    w, h = template.shape[::-1]

    # Establecer un umbral de coincidencia
    

    # Realizar la coincidencia de plantillas
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

    # Encontrar ubicaciones donde la coincidencia es mayor que el umbral
    #threshold = 0.95
    threshold = 0.7
    loc = np.where(res >= threshold)

    # Imprimir las coordenadas de coincidencia
    #for pt in zip(*loc[::-1]):
        #print("Coincidencia encontrada en las coordenadas:", pt)

    # Verificar si hay coincidencias
    if len(loc[0]) > 0:
        
        #print("Se encontró al menos una coincidencia.")
        # Tomar la primera coincidencia
        pt = (loc[1][0], loc[0][0])
        # Dibujar un rectángulo alrededor de la primera coincidencia
        cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        center_x = left+ pt[0] + w // 2
        center_y = top + pt[1] + h // 2
        print(f'{template_path} {len(loc[0]) > 0}, x={center_x}, x={center_y}')
        cv2.imshow('Detected', screenshot)





    # Dibujar un rectángulo alrededor de la región coincidente
    #for pt in zip(*loc[::-1]):
    #    cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        
    #    center_x = left+ pt[0] + w // 2
    #    center_y = top + pt[1] + h // 2
        #pydirectinput.click(center_x,center_y)
        #time.sleep(0.1)
        
        
        

    # devuelvo si hay concidencias
    return screenshot,len(loc[0]) > 0,center_x,center_y

# Título de la ventana del programa de Windows
window_title = "NIGHT CROWS(1)"

# Ruta de la plantilla del objeto que deseas detectar
#template_path = 'btn_todos.png'

# Obtener la ventana del programa de Windows por su título
window = gw.getWindowsWithTitle(window_title)[0]

cont =0
cant_encargos=0
# Bucle principal
while True:

    if cont==400:
        
        template_path = 'btn_salir.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)
 
        if encontre:
            pydirectinput.click(x,y)
            time.sleep(1)
        
        template_path = 'btn_almacen.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)
 
        if encontre:
            pydirectinput.click(x,y)
            time.sleep(2)
        
        template_path = 'btn_peticiones.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)
 
        if encontre:
            pydirectinput.click(x,y)
            time.sleep(3)
        
        template_path = 'btn_enc.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)
 
        if encontre:
            pydirectinput.click(x,y)
            time.sleep(1)
        
        template_path = 'btn_check.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)    

        if encontre:
            pydirectinput.click(x,y)
            time.sleep(0.1)        
        
        
        
        cont=0
    else:

        # Detectar el objeto y obtener la imagen con el objeto detectado
        template_path = 'encargos_completados.png'
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)
    
        # Mostrar la imagen con el objeto detectado
        #cv2.imshow('Detected', detected_image)
        #print(f'{template_path} {encontre}, x={x}, x={y}')
        
        if encontre:
            print(f'{datetime.datetime.now()} Encargos completados ')
            break
        #    pydirectinput.click(x,y)
        #    time.sleep(0.3)




        # Detectar el objeto y obtener la imagen con el objeto detectado
        template_path = 'btn_todos.png'
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)
    
        # Mostrar la imagen con el objeto detectado
        #cv2.imshow('Detected', detected_image)
        #print(f'{template_path} {encontre}, x={x}, x={y}')
        
        if encontre:
            pydirectinput.click(x,y)
            time.sleep(0.3)
    
        template_path = 'btn_yunque.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)
 
        if encontre:
            pydirectinput.click(x,y)
            time.sleep(0.1)
            pydirectinput.click(x,y)
            time.sleep(0.1)
    
        template_path = 'btn_fabricar.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)    

        if encontre:
            pydirectinput.click(x,y)
            time.sleep(0.1)
            pydirectinput.press('y')
            time.sleep(0.1)
 
        template_path = 'btn_cruz.png'    
        detected_image,encontre,x,y = detect_object(window, template_path,0.9)    

        if encontre:
            print(f'{datetime.datetime.now()} Encargo exitoso')
            pydirectinput.click(x,y)
            time.sleep(0.1)
            
            
            
    print(f'Intento:{cont}')
    cont=cont+1

    # Esperar y capturar la tecla de salida (Esc) para detener el bucle
    if cv2.waitKey(500) == 27:
        break

cv2.destroyAllWindows()