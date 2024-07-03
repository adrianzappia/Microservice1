import cv2
import numpy as np
import pyautogui
import pygetwindow

# Obtener la ventana de la aplicación por su título
app_window = pygetwindow.getWindowsWithTitle("NIGHT CROWS(1)")[0]

# Definir las coordenadas de la ventana
x, y, width, height = app_window.left, app_window.top, app_window.width, app_window.height

while True:
    # Tomar una captura de pantalla de la ventana de la aplicación
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Convertir la captura de pantalla a una matriz numpy
    frame = np.array(screenshot)

    # Obtener la posición actual del mouse
    mouse_x, mouse_y = pyautogui.position()

    # Mostrar las coordenadas del mouse en la consola
    print(f"Coordenadas del mouse: ({mouse_x}, {mouse_y})")

    # Mostrar la captura de pantalla con OpenCV
    cv2.imshow('Captura de ventana', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar la ventana
cv2.destroyAllWindows()