import pydirectinput
import time

# Función para hacer clic en la posición actual del cursor y mostrar las coordenadas
def hacer_clic_en_posicion_actual():
    # Obtiene las coordenadas actuales del cursor
    x, y = pydirectinput.position()
    
    # Imprime las coordenadas actuales del cursor
    print(f"Coordenadas del cursor: ({x}, {y})")
    
    # Hace clic en las coordenadas actuales del cursor
    pydirectinput.click(x, y)

# Loop infinito para hacer clic cada 5 segundos
while True:
    hacer_clic_en_pcosicion_actual()
    time.sleep(5)