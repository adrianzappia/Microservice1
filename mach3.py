import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import time
import pydirectinput
import pytesseract



# Función para detectar el objeto y obtener las coordenadas de coincidencia
def detect_object(window, template_path):
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
    threshold = 0.9
    loc = np.where(res >= threshold)

    # Imprimir las coordenadas de coincidencia
    for pt in zip(*loc[::-1]):
        print("Coincidencia encontrada en las coordenadas:", pt)

    # Dibujar un rectángulo alrededor de la región coincidente
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        
        center_x = left+ pt[0] + w // 2
        center_y = top + pt[1] + h // 2
        #pydirectinput.click(center_x,center_y)
        #time.sleep(0.1)
        
    
        #pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OC\\tesseract.exe'
    
        #Extraer la región de la imagen donde se encontró la coincidencia
        region_of_interest = gray[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
        #cv2.imshow('muestro',region_of_interest )
        #Aplicar OCR a la región de interés
        #extracted_text = pytesseract.image_to_string(region_of_interest)
        
        #Imprimir el texto extraído
        #print("Texto extraído:", extracted_text)





        # Asumiendo que pt contiene las coordenadas de la esquina superior izquierda de la región detectada
       # x, y = pt[0]-4, pt[1]  # Coordenadas x e y de la esquina superior izquierda
        #width = w  # Ancho de la región detectada
        #height = h  # Altura de la región detectada

        # Calcular las coordenadas de la esquina superior izquierda del cuadrado a la derecha
        #new_x = x + width  # La coordenada x del cuadrado a la derecha es el final de la región detectada
        #new_y = y  # La coordenada y del cuadrado a la derecha es la misma que la región detectada

        # Calcular el tamaño del cuadrado (mismo tamaño que la región detectada)
       # new_width = width-60
        #new_height = height
        
        # Obtener la región cuadrada a la derecha
        #region_to_right = gray[new_y:new_y+new_height, new_x:new_x+new_width]
        #cv2.imshow('muestro',cv2.bitwise_not(region_to_right) )
          
        
        
        
        #Aplicar OCR a la región de interés
        #texto = pytesseract.image_to_string(cv2.bitwise_not(region_to_right), config='--psm 6 --oem 3')
        
        #Imprimir el texto extraído
        #print("Texto extraído:", texto)




















    
        

    # Devolver la imagen con el objeto detectado
    return screenshot

# Título de la ventana del programa de Windows
window_title = "NIGHT CROWS(1)"

# Ruta de la plantilla del objeto que deseas detectar
#template_path = 'nv.png' 0.9
template_path = 'saltar.png' 

# Obtener la ventana del programa de Windows por su título
window = gw.getWindowsWithTitle(window_title)[0]

# Bucle principal
while True:
    # Detectar el objeto y obtener la imagen con el objeto detectado
    detected_image = detect_object(window, template_path)

    # Mostrar la imagen con el objeto detectado
    cv2.imshow('Detected', detected_image)

    # Esperar y capturar la tecla de salida (Esc) para detener el bucle
    if cv2.waitKey(500) == 27:
        break

cv2.destroyAllWindows()