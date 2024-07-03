import pyautogui
import time

# Función para hacer clic en la posición actual del cursor
def hacer_clic_en_posicion_actual():
    # Obtiene las coordenadas actuales del cursor
    x, y = pyautogui.position()
    print(x,y)
    # Hace clic en las coordenadas actuales del cursor
    pyautogui.click(x, y)
    

# Loop infinito para hacer clic cada 5 segundos
while True:
    hacer_clic_en_posicion_actual()
    time.sleep(5)