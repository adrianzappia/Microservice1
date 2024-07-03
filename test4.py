import time
import threading
import tkinter as tk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.stopped = False

    def on_created(self, event):
        if not event.is_directory:
            print(f"Archivo creado: {event.src_path}")
            # Agrega aquí el código para procesar el archivo recién creado

    def stop(self):
        self.stopped = True

def start_monitoring(directory):
    handler = MyHandler()
    observer = Observer()
    observer.schedule(handler, path=directory, recursive=False)
    observer.start()

    try:
        while not handler.stopped:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

def stop_monitoring():
    global monitoring_thread
    if monitoring_thread is not None and monitoring_thread.is_alive():
        monitoring_thread.join()

def start_button_click():
    global monitoring_thread
    directory = entry.get()
    monitoring_thread = threading.Thread(target=start_monitoring, args=(directory,))
    monitoring_thread.start()

def stop_button_click():
    stop_monitoring()

root = tk.Tk()
root.title("Monitor de Ficheros")
root.geometry("400x150")

label = tk.Label(root, text="Directorio a monitorear:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

start_button = tk.Button(root, text="Iniciar Monitoreo", command=start_button_click)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Detener Monitoreo", command=stop_button_click)
stop_button.pack(pady=10)

monitoring_thread = None

root.mainloop()