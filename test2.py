from zeep import Client, Settings
from requests.auth import HTTPBasicAuth

# URL del servicio SOAP
url = 'http://ventas.costaurbana.com.uy/soap/NodumLocales/services/sim/v1.3/wsConsxRUT?wsdl'

# Credenciales de autenticación HTTP básica
username = 'FINICUS'
password = 'Na2T93I4v!O'
numero_rut = '214644170010'

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
print(resultado)
print(len(resultado))
print(len(resultado[0].R_General))
print(len(resultado[0].R_General.R_Det))


CodShopping = resultado[0].R_General.R_Det[0].R_CodigoShopping
NroContrato = resultado[0].R_General.R_Det[0].R_NumerodeContrato

print('Codigo Shopping',CodShopping)
print('Numero de contrato',NroContrato)
# Acceder al primer elemento de la lista

#r_general = resultado[0].R_wsConsxRUT[0].R_General
#numero_rut_respuesta = r_general.R_Cab.R_NumeroRUT

#print(resultado)


url2='http://ventas.costaurbana.com.uy/soap/NodumLocales/services/sim/v1.3/wsConsxCont?wsdl'
session = Session()
session.auth = HTTPBasicAuth(username, password)
client = Client(url2,transport=Transport(session=session))
resultado = client.service.simular(wsConsxCont={'General': {'Cab': {'NumeroRUT': numero_rut, 'CodigoShopping': CodShopping, 'NumeroContrato': NroContrato }}})
print(resultado)
print(len(resultado))


url3='http://ventas.costaurbana.com.uy/soap/NodumLocales/services/sim/v1.3/wsConsxCont?wsdl'
session = Session()
session.auth = HTTPBasicAuth(username, password)
client = Client(url2,transport=Transport(session=session))
resultado = client.service.simular(wsConsxCont={'General': {'Cab': {'NumeroRUT': numero_rut, 'CodigoShopping': '02', 'NumeroContrato':  '230862' }}})
print(resultado)
print(len(resultado))


print("************************************ LAS PIEDRAS SHOPPING *********************************************************")

username = 'FINI'
password = 'fRo1ote0IFrO'
numero_rut = '214644170010'

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
print(resultado)
print(len(resultado))
print(len(resultado[0].R_General))
print(len(resultado[0].R_General.R_Det))

CodShopping = resultado[0].R_General.R_Det[0].R_CodigoShopping
NroContrato = resultado[0].R_General.R_Det[0].R_NumerodeContrato

CodShopping1 = resultado[0].R_General.R_Det[1].R_CodigoShopping
NroContrato1 = resultado[0].R_General.R_Det[1].R_NumerodeContrato

print('Codigo Shopping',CodShopping)
print('Numero de contrato',NroContrato)
# Acceder al primer elemento de la lista

#r_general = resultado[0].R_wsConsxRUT[0].R_General
#numero_rut_respuesta = r_general.R_Cab.R_NumeroRUT

#print(resultado)


url2='http://ventas.costaurbana.com.uy/soap/NodumLocales/services/sim/v1.3/wsConsxCont?wsdl'
session = Session()
session.auth = HTTPBasicAuth(username, password)
client = Client(url2,transport=Transport(session=session))
resultado = client.service.simular(wsConsxCont={'General': {'Cab': {'NumeroRUT': numero_rut, 'CodigoShopping': CodShopping, 'NumeroContrato': NroContrato }}})
print(resultado)
print(len(resultado))


url3='http://ventas.costaurbana.com.uy/soap/NodumLocales/services/sim/v1.3/wsConsxCont?wsdl'
session = Session()
session.auth = HTTPBasicAuth(username, password)
client = Client(url2,transport=Transport(session=session))
resultado = client.service.simular(wsConsxCont={'General': {'Cab': {'NumeroRUT': numero_rut, 'CodigoShopping': CodShopping1, 'NumeroContrato':  NroContrato1 }}})
print(resultado)
print(len(resultado))






"""



#envio de factura

url3 = 'https://ventas.costaurbana.com.uy/soap/NodumLocales/services/forms/v1.3/wsDeclaVtas?wsdl'
session = Session()
session.auth = HTTPBasicAuth(username, password)
client = Client(url2,transport=Transport(session=session))

# Preparar los parámetros de entrada para la función "procesarAlta"
entrada = {
    "General": {
        "Cab": {
            "NumeroRUT": "123456789",
            "CodigoShopping": "ABC123",
            "NumeroContrato": 123,
            "CodigoCanal": "XYZ",
            "Secuencial": 456,
            "Caja": "Caja001",
            "Nombredecliente": "Cliente ABC",
            "NrodeTelefono": "1234567890",
            "CodigoCFE": 101,
            "NumeroCFE": 101112,
            "SerieCFE": "A",
            "DocIdCFE": "Doc001",
            "MonedaCFE": "USD",
            "FechaEmisionCFE": "2023-07-27",
            "TotalMOCIVA": 100.0,
            "TotalMNSIVA": 80.0,
            "CodigoFormaPago": "Efectivo",
            "Numerodepromo": "Promo123",
            "FechaTransferencia": "2023-07-27",
            "Horatransferencia": "08:30:00",
            "CantidadCuotas": 1,
            "ObsCab1": "Observación 1",
            "ObsCab2": "Observación 2"
        },
        "Det": [
            {
                "CodRubro": "Rubro1",
                "ContadoMNSIVA": 50.0,
                "CreditoMNSIVA": 30.0,
                "DebitoMNSIVA": 20.0,
                "IncluirenPromo": True,
                "ObsLin1": "Observación 1",
                "ObsLin2": "Observación 2"
            },
            {
                "CodRubro": "Rubro2",
                "ContadoMNSIVA": 40.0,
                "CreditoMNSIVA": 20.0,
                "DebitoMNSIVA": 20.0,
                "IncluirenPromo": False,
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
if resultado and resultado.Resultado:
    for item in resultado.Resultado:
        estado = item.estado
        mensaje = item.mensaje
        identificador = item.identificador
        print(f"Estado: {estado}, Mensaje: {mensaje}, Identificador: {identificador}")
else:
    print("El resultado no contiene datos.")

"""
