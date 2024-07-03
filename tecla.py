import time
import pyautogui

def presionar_tecla(tecla):
    # Simula la presión de la tecla especificada
    pyautogui.press(tecla)

# Función principal
def main():
    # Tecla que deseas presionar
    tecla = '4'

    # Tiempo entre cada presión de tecla (en segundos)
    intervalo = 5  # Presionar la tecla "4" cada 5 segundos

    try:
        while True:
            presionar_tecla(tecla)
            print("Tecla", tecla, "presionada")
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")

if __name__ == "__main__":
    main()44