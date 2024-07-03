print ("hola mundo")

#from suds.client import Client
from requests.auth import HTTPBasicAuth
import requests
from suds.client import Client

# Reemplaza 'URL_DEL_WSDL' por la URL real del archivo WSDL del servicio web que deseas consumir.
url_del_wsdl = 'http://ventas.costaurbana.com.uy/soap/NodumLocales/services/sim/v1.3/wsConsxRUT?wsdl'
username = 'FINI'
password = 'fRo1ote0IFrO'

# Crea una instancia del cliente SOAP.
client = Client(url_del_wsdl)
settings = Settings(strict=False, xml_huge_tree=True)
# Agrega las credenciales de autenticación básica al encabezado de la solicitud HTTP.
client.set_options(headers={"Authorization": HTTPBasicAuth(username, password)})

#try:
#    for service in client.wsdl.services.values():
#        for port in service.ports.values():
#            for operation in port.binding._operations.values():
#                print(operation.name)
#
#except Exception as e:
#    print(f"Error: {e}")


Ñ