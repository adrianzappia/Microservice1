import pyautogui
import time

# Función para obtener y mostrar las coordenadas del clic
def mostrar_coordenadas_clic():
    # Obtiene las coordenadas del clic
    x, y = pyautogui.position()

# Hace clic en las coordenadas actuales del cursor
    pyautogui.click(x, y)



    # Muestra las coordenadas del clic
    print(f"Coordenadas del clic: ({x}, {y})")

# Loop infinito para mostrar las coordenadas del clic cada 5 segundos
while True:
    mostrar_coordenadas_clic()
    time.sleep(5)  # Espera 5 segundos antes de mostrar las coordenadas nuevamente
