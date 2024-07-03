from requests import Session
from zeep import Client
from zeep.transports import Transport
from zeep import Client
from zeep.plugins import HistoryPlugin
from requests.auth import HTTPBasicAuth  # Importa HTTPBasicAuth para autenticación básica

# URL del servicio web SOAP
url = 'https://ventas.costaurbana.com.uy/soap/NodumLocales/services/forms/v1.3/wsDeclaVtas?wsdl'

# Credenciales de autenticación (usuario y contraseña)
usuario = 'FINI'
contra = ''

# Crear un cliente SOAP con un plugin de historial para depuración
session = Session()
session.auth = HTTPBasicAuth(usuario, contra)
client = Client(url,transport=Transport(session=session))


# Preparar los parámetros de entrada para la función "procesarAlta"
entrada = {
    "General": {
        "Cab": {
            "NumeroRUT": "214644170010",
            "CodigoShopping": "01",
            "NumeroContrato": 100391,
            "CodigoCanal": "1",
            "Secuencial": 457,
            "Caja": "Caja001",
            "Nombredecliente": "Cliente ABC",
            "NrodeTelefono": "1234567890",
            "CodigoCFE": 101,
            "NumeroCFE": 101113,
            "SerieCFE": "A",
            "DocIdCFE": "Doc001",
            "MonedaCFE": "USD",
            "FechaEmisionCFE": "2023-07-27",
            "TotalMOCIVA": 122.0,
            "TotalMNSIVA": 100.0,
            "CodigoFormaPago": "00",
            "Numerodepromo": "Promo123",
            "FechaTransferencia": "2023-07-27",
            "Horatransferencia": "08:30",
            "CantidadCuotas": 1,
            "ObsCab1": "Observación 1",
            "ObsCab2": "Observación 2"
        },
        "Det": [
            {
                "CodRubro": "84",
                "ContadoMNSIVA": 51.0,
                "CreditoMNSIVA": 0.0,
                "DebitoMNSIVA": 0.0,
                "IncluirenPromo": "N",
                "ObsLin1": "Observación 1",
                "ObsLin2": "Observación 2"
            },
            {
                "CodRubro": "84",
                "ContadoMNSIVA": 49.0,
                "CreditoMNSIVA": 0.0,
                "DebitoMNSIVA": 0.0,
                "IncluirenPromo": "N",
                "ObsLin1": "Observación 1",
                "ObsLin2": "Observación 2"
            }
            # Puedes agregar más elementos de detalle si es necesario
        ]
    }
}

# Llamar a la función "procesarAlta" del servicio web SOAP
resultado = client.service.procesarAlta(wsDeclaVtas=entrada)

# Verificar si el resultado contiene datos
if resultado:
    for item in resultado:
        estado = item.estado
        mensaje = item.mensaje
        identificador = item.identificador
        print(f"Estado: {estado}, Mensaje: {mensaje}, Identificador: {identificador}")
else:
    print("El resultado está vacío o no contiene datos.")