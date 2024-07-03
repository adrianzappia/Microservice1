import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

# Obtener la ventana del programa de Windows por su título
window_title = "NIGHT CROWS(1)"
window = gw.getWindowsWithTitle(window_title)[0]

# Obtener las dimensiones de la ventana
left, top, width, height = window.left, window.top, window.width, window.height

# Capturar la pantalla dentro de la ventana del programa
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Cargar la plantilla del objeto que deseas detectar
template = cv2.imread('ejemplo.png', 0)

# Obtener las dimensiones de la plantilla
w, h = template.shape[::-1]

# Realizar la coincidencia de plantillas
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

# Establecer un umbral de coincidencia
threshold = 0.8
loc = np.where(res >= threshold)

# Dibujar un rectángulo alrededor de la región coincidente
for pt in zip(*loc[::-1]):
    cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Mostrar la imagen con el objeto detectado
cv2.imshow('Detected', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()