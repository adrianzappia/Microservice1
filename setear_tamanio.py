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

# Redimensionar la ventana
window.resizeTo(989, 624)
