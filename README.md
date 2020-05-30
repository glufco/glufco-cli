GUIA DE INTEGRACION GLUFCO


INTRODUCCION

El criptoactivo glufco -GLF- es un token creado en la cadena de bloques de la Plataforma WAVES. En tal sentido, la integración de glufco está fundamentada por la integración de WAVES a su plataforma de criptomonedas.

Al utilizar las recomendaciones de esta guía, usted podrá operar la criptomoneda WAVES, así como también cualquier token (asset) creado en esta cadena de bloques.


DOCUMENTACION OFICIAL

La información general de WAVES se encuentra en 
•	https://wavesplatform.com/

La documentación oficial de WAVES en 
•	https://docs.wavesplatform.com/en/

WAVES dispone de diversas librerías para su integración, para glufco hemos utilizado las librerías Python “PyWaves”, que proveen una completa documentación. Toda la información técnica en:
•	https://docs.wavesplatform.com/en/building-apps/waves-api-and-sdk/client-libraries/
•	https://docs.wavesplatform.com/en/building-apps/waves-api-and-sdk/client-libraries/pywaves

•	https://pypi.org/project/PyWaves/
•	https://github.com/PyWaves/PyWaves

Adicionalmente, se utiliza la librería Python Cryptos.
•	https://pypi.org/project/cryptos/
•	https://github.com/topics/cryptos


GUIA DE INSTALACION

En Glufco hemos desarrollado un script que permite interactuar con la librería WAVES en modo CLI, para servidores Linux. Este script ha sido desarrollado y está en producción en Servidores Linux Ubuntu 18.04 LTC y Python 3.6.
Este sistema aún está en optimización, con el que queremos lograr un completo manejo de otras criptomonedas, de otros WAVES Assets y una instalación automática a través de los comandos Linux. Actualmente, seguiremos un paso a paso de instalación.

Se deben instalar las librerías utilizando Python pip3
•	sudo pip3 install pywaves
•	sudo pip3 install cryptos

Se copian dos (02) archivos:
•	glufco
o	Archivo ejecutable que toma los argumentos del CLI y los entrega al script Python.
o	Con usuario administrador se debe copiar en la carpeta /bin.
o	Con usuario administrador se debe dar atributos de archivo ejecutable: 
	sudo chmod +x /bin/glufco

•	glufco.py
o	Script Python.
o	Con usuario administrador se debe copiar en la carpeta /etc.


GUIA DE USO

Con los pasos anteriores, el sistema queda configurado con una implementación de las librerías PyWaves para ser utilizadas por la consola del sistema. Todas las respuestas son en formato JSON. Por ejemplo:

ubuntu@criptolago:~$ glufco balance 3P4SAj1fh87uYeHcEWTSUJgA251MGcAyPoE
{"network": "WAVES", "address": "3P4SAj1fh87uYeHcEWTSUJgA251MGcAyPoE", "waves": "733.04260008", "glufco": "20.0"}



A continuación todos los comandos disponibles:
 
Glufco Investment
A brilliant python3: pywaves and cryptos implementation for
glufco/waves/bitcoin/litecoin/dash and other waves assets

Commands usage:
balance      Get waves and glufco address balance
             args: address
newaddress   Create a new waves, bitcoin, litecoin or dash address
             with random or given seed
             args: coin=waves/bitcoin/litecoin/dash
                   seed=(optional)'a big long brainwallet password'
help         This help
sendglf      Send glufco from user1 to user2
             args: user1privKey - Sender private key
                   user2Address - Destination address
                   amount - Amount to send. Example: 100 for 1 glufco
                   message(optional)
             Transfer Fee = 0.1 glufco
sendwaves    Send waves from user1 to user2
             args: user1privKey - Sender private key
                   user2Address - Destination address
                   amount - Amount to send. Ex: 100000000 for 1 waves
             Transfer Fee = 0.001 waves
validate     Validate address
             args: coin=waves
                   address
version      Version





