from suds.client import Client
from suds.wsse import Security, UsernameToken

from suds.client import Client
from suds.sax.text import Raw
from suds.transport.http import HttpAuthenticated
from suds.transport.https import HttpAuthenticated
import urllib2



# URL del servicio web SOAP
url = "https://ventas.costaurbana.com.uy/soap/NodumLocales/services/forms/v1.3/wsDeclaVtas?wsdl"

# Crear un cliente SOAP
client = Client(url)

# Configurar autenticacion con usuario y clave
#security = Security()
#token = UsernameToken('FINI','fRo1ote0IFrO')
#security.tokens.append(token)
#client.set_options(wsse=security)

t = HttpAuthenticated(username='FINI', password='fRo1ote0IFrO')
t.handler = urllib2.HTTPBasicAuthHandler(t.pm)
t.urlopener = urllib2.build_opener(t.handler)
client = Client(url=url, transport=t)




# Configurar los datos de solicitud (rellena con tus datos)
request = client.factory.create('xsd1:entrada')


entrada = {
    "General": {
        "Cab": {
            "NumeroRUT": "214644170010",
            "CodigoShopping": "01",
            "NumeroContrato": 100391,
            "CodigoCanal": "1",
            "Secuencial": 458,
            "Caja": "Caja001",
            "Nombredecliente": "Cliente ABC",
            "NrodeTelefono": "1234567890",
            "CodigoCFE": 101,
            "NumeroCFE": 101117,
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
            "ObsCab1": "Observacion 1",
            "ObsCab2": "Observacion 2"
        },
        "Det": [
            {
                "CodRubro": "84",
                "ContadoMNSIVA": 51.0,
                "CreditoMNSIVA": 0.0,
                "DebitoMNSIVA": 0.0,
                "IncluirenPromo": "N",
                "ObsLin1": "Observacion 1",
                "ObsLin2": "Observacion 2"
            },
            {
                "CodRubro": "84",
                "ContadoMNSIVA": 49.0,
                "CreditoMNSIVA": 0.0,
                "DebitoMNSIVA": 0.0,
                "IncluirenPromo": "N",
                "ObsLin1": "Observacion 1",
                "ObsLin2": "Observacion 2"
            }
            # Puedes agregar mas elementos de detalle si es necesario
        ]
    }
}



#request.wsDeclaVtas.append(entrada)
# Llamar al metodo del servicio web (procesarAlta)
response = client.service.procesarAlta(entrada)





# Imprimir la respuesta
#print(response)


# Itera a traves de los elementos de la respuesta (si es una lista)
for elemento in response:
    estado = elemento.estado
    mensaje = elemento.mensaje
    identificador = elemento.identificador
