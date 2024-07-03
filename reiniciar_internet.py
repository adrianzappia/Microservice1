import requests
from bs4 import BeautifulSoup

# Configuración del router
router_url = "http://192.168.0.1"  # URL base del router
login_url = router_url + "/webpages/login.html"  # URL específica del formulario de inicio de sesión
router_password = "Lukesw"   # Cambia "contraseña" por tu contraseña para el router

# Datos del formulario de inicio de sesión
login_data = {
    "password": router_password
}

# Iniciar una sesión
session = requests.Session()

# Enviar una solicitud POST para iniciar sesión
response = session.post(login_url, data=login_data)
print(response.content)

# Verificar si el inicio de sesión fue exitoso
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    welcome_message = soup.find('input', {'id': 'internet_status'})
    if welcome_message:
        print("Inicio de sesión exitoso")
    else:
        print("Error: No se encontró el mensaje de bienvenida")
else:
    print("Error al iniciar sesión")