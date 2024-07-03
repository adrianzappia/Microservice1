import tkinter as tk
from tkinter import ttk
import configparser

def boton1_presionado():

    url = valor1_entry.get() 
    username = valor2_entry.get()
    password = valor3_entry.get()
    numero_rut = valor4_entry.get()

    from requests import Session
    from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
    from zeep import Client
    from zeep.transports import Transport

    session = Session()
    session.auth = HTTPBasicAuth(username, password)
    client = Client(url,transport=Transport(session=session))


    # Llamar a la función "simular" del servicio web SOAP
    resultado = client.service.simular(wsConsxRUT={'General': {'Cab': {'NumeroRUT': numero_rut}}})

    # Imprimir el resultado (ten en cuenta que el resultado dependerá de la implementación del servicio)
    #print(resultado)
    #print(len(resultado))
    #print(len(resultado[0].R_General))
    #print(len(resultado[0].R_General.R_Det))


    resultado_text.config(state=tk.NORMAL)
    resultado_text.insert(tk.END,resultado)
    resultado_text.config(state=tk.DISABLED)

def boton2_presionado():
    resultado_text.config(state=tk.NORMAL)
    resultado_text.insert(tk.END, "¡Botón 2 presionado!\n")
    resultado_text.config(state=tk.DISABLED)

def obtener_valores():
    valor1 = valor1_entry.get()
    valor2 = valor2_entry.get()
    valor3 = valor3_entry.get()
    valor4 = valor4_entry.get()
    resultado_text.config(state=tk.NORMAL)
    resultado_text.insert(tk.END, f"URL: {valor1}\nUsuario: {valor2}\nContraseña: {valor3}\nRUT: {valor4}\n")
    resultado_text.config(state=tk.DISABLED)

def guardar_valores():
    valor1 = valor1_entry.get()
    valor2 = valor2_entry.get()
    valor3 = valor3_entry.get()
    valor4 = valor4_entry.get()

    config = configparser.ConfigParser()
    config['Campos'] = {
        'URL': valor1,
        'Usuario': valor2,
        'Contraseña': valor3,
        'RUT': valor4
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def salir():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Solapas")

# Leer los campos desde el archivo de configuración
config = configparser.ConfigParser()
config.read('config.ini')
url_value = config.get('Campos', 'URL', fallback='')
usuario_value = config.get('Campos', 'Usuario', fallback='')
password_value = config.get('Campos', 'Contraseña', fallback='')
rut_value = config.get('Campos', 'RUT', fallback='')

# Crear un notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Solapa 1
pagina1 = ttk.Frame(notebook)
notebook.add(pagina1, text="Solapa 1")

# Crear los botones y el área de texto en la primera página
resultado_text = tk.Text(pagina1, wrap=tk.WORD)
resultado_text.pack(fill=tk.BOTH, expand=True)
resultado_text.config(state=tk.DISABLED)

boton1 = tk.Button(pagina1, text="Botón 1", command=boton1_presionado)
boton1.pack(side=tk.LEFT, padx=5)

boton2 = tk.Button(pagina1, text="Botón 2", command=boton2_presionado)
boton2.pack(side=tk.LEFT, padx=5)

# Solapa 2
pagina2 = ttk.Frame(notebook)
notebook.add(pagina2, text="Solapa 2")

# Crear los campos de entrada en la segunda página
valor1_label = tk.Label(pagina2, text="URL:")
valor1_label.pack(pady=5)
valor1_entry = tk.Entry(pagina2)
valor1_entry.pack(pady=5)
valor1_entry.insert(0, url_value)

valor2_label = tk.Label(pagina2, text="Usuario:")
valor2_label.pack(pady=5)
valor2_entry = tk.Entry(pagina2)
valor2_entry.pack(pady=5)
valor2_entry.insert(0, usuario_value)

valor3_label = tk.Label(pagina2, text="Contraseña:")
valor3_label.pack(pady=5)
valor3_entry = tk.Entry(pagina2, show="*")
valor3_entry.pack(pady=5)
valor3_entry.insert(0, password_value)

valor4_label = tk.Label(pagina2, text="RUT:")
valor4_label.pack(pady=5)
valor4_entry = tk.Entry(pagina2)
valor4_entry.pack(pady=5)
valor4_entry.insert(0, rut_value)

# Botón para obtener valores en la segunda página
obtener_valores_boton = tk.Button(pagina2, text="Obtener Valores", command=obtener_valores)
obtener_valores_boton.pack(pady=5)

# Botón para guardar valores en el archivo de configuración
guardar_valores_boton = tk.Button(pagina2, text="Guardar", command=guardar_valores)
guardar_valores_boton.pack(pady=5)

# Configurar el sistema de geometría de Tkinter para adaptarse al cambio de tamaño
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Iniciar el bucle de eventos
ventana.mainloop()