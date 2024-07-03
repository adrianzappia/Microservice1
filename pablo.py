import tkinter as tk

def guardar_datos():
    datos = {
        "NumeroRUT": entrada_numero_rut.get(),
        "CodigoShopping": entrada_codigo_shopping.get(),
        "NumeroContrato": entrada_numero_contrato.get(),
        "CodigoCanal": entrada_codigo_canal.get(),
        "Secuencial": entrada_secuencial.get(),
        "Caja": entrada_caja.get(),
        "Nombredecliente": entrada_nombre_cliente.get(),
        "NrodeTelefono": entrada_numero_telefono.get(),
        "CodigoCFE": entrada_codigo_cfe.get(),
        "NumeroCFE": entrada_numero_cfe.get(),
        "SerieCFE": entrada_serie_cfe.get(),
        "DocIdCFE": entrada_doc_id_cfe.get(),
        "MonedaCFE": entrada_moneda_cfe.get(),
        "FechaEmisionCFE": entrada_fecha_emision_cfe.get(),
        "TotalMOCIVA": entrada_total_moc_iva.get(),
        "TotalMNSIVA": entrada_total_mn_siva.get(),
        "CodigoFormaPago": entrada_codigo_forma_pago.get(),
        "Numerodepromo": entrada_numero_promo.get(),
        "FechaTransferencia": entrada_fecha_transferencia.get(),
        "Horatransferencia": entrada_hora_transferencia.get(),
        "CantidadCuotas": entrada_cantidad_cuotas.get(),
        "ObsCab1": entrada_obs_cab1.get(),
        "ObsCab2": entrada_obs_cab2.get(),
    }

    with open("datos.txt", "w") as archivo:
        for clave, valor in datos.items():
            archivo.write(f"{clave}: {valor}\n")

    etiqueta_confirmacion.config(text="Datos guardados en datos.txt")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Captura de Datos")

# Crear 4 frames para organizar los elementos en 4 columnas
frame1 = tk.Frame(ventana)
frame2 = tk.Frame(ventana)
frame3 = tk.Frame(ventana)
frame4 = tk.Frame(ventana)

# Crear etiquetas y campos de entrada para los datos
etiqueta_numero_rut = tk.Label(frame1, text="NumeroRUT:")
entrada_numero_rut = tk.Entry(frame1)

etiqueta_codigo_shopping = tk.Label(frame1, text="CodigoShopping:")
entrada_codigo_shopping = tk.Entry(frame1)

etiqueta_numero_contrato = tk.Label(frame2, text="NumeroContrato:")
entrada_numero_contrato = tk.Entry(frame2)

etiqueta_codigo_canal = tk.Label(frame2, text="CodigoCanal:")
entrada_codigo_canal = tk.Entry(frame2)

etiqueta_secuencial = tk.Label(frame3, text="Secuencial:")
entrada_secuencial = tk.Entry(frame3)

etiqueta_caja = tk.Label(frame3, text="Caja:")
entrada_caja = tk.Entry(frame3)

etiqueta_nombre_cliente = tk.Label(frame4, text="Nombredecliente:")
entrada_nombre_cliente = tk.Entry(frame4)

etiqueta_numero_telefono = tk.Label(frame4, text="NrodeTelefono:")
entrada_numero_telefono = tk.Entry(frame4)

# Continuar creando etiquetas y campos de entrada para los demás datos...

# Botón para guardar los datos
boton_grabar = tk.Button(ventana, text="Grabar", command=guardar_datos)

# Etiqueta para mostrar la confirmación
etiqueta_confirmacion = tk.Label(ventana, text="")

# Organizar elementos en las columnas
frame1.pack(side=tk.LEFT, padx=10, pady=10)
frame2.pack(side=tk.LEFT, padx=10, pady=10)
frame3.pack(side=tk.LEFT, padx=10, pady=10)
frame4.pack(side=tk.LEFT, padx=10, pady=10)

# Organizar el botón y etiqueta de confirmación en la parte inferior
boton_grabar.pack(pady=10)
etiqueta_confirmacion.pack()

ventana.mainloop()