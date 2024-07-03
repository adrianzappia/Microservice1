import tkinter as tk
import csv
import os

def grabar_datos():
    # Obtener los valores de los campos de entrada
    valor1 = entry1.get()
    valor2 = entry2.get()
    valor3 = entry3.get()

    # Definir la ruta del archivo CSV
    ruta_csv = r'C:\prueba\factura.csv'

    # Verificar si la carpeta de destino existe, si no, crearla
    carpeta_destino = os.path.dirname(ruta_csv)
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Abrir el archivo CSV en modo de escritura
    with open(ruta_csv, 'a', newline='') as archivo_csv:
        # Crear un objeto escritor CSV
        escritor = csv.writer(archivo_csv)

        # Escribir los datos en el archivo CSV
        escritor.writerow([valor1, valor2, valor3])

    # Borrar los campos de entrada después de grabar los datos
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Grabar Datos en CSV")

# Crear campos de entrada
label1 = tk.Label(ventana, text="Valor 1:")
label1.pack()
entry1 = tk.Entry(ventana)
entry1.pack()

label2 = tk.Label(ventana, text="Valor 2:")
label2.pack()
entry2 = tk.Entry(ventana)
entry2.pack()

label3 = tk.Label(ventana, text="Valor 3:")
label3.pack()
entry3 = tk.Entry(ventana)
entry3.pack()

# Crear un botón para grabar los datos
boton_grabar = tk.Button(ventana, text="Grabar", command=grabar_datos)
boton_grabar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()