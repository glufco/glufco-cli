# Glufco Investment Cryptobank
# Use Python 3.6 
# When installing pywaves and cryptos use: sudo pip3 install pywaves cryptos
version = "Glufco 1.2 - Use: Python=3.6.8, PyWaves=0.8.25, cryptos=1.36"
# [DK] 05/2020 www.glufco.com

import sys
import json
import pywaves as pw
from cryptos import *
#connects to mainnet node
pw.setNode(node = 'https://nodes.wavesplatform.com', chain = 'mainnet')
#connects to testnet node
# pw.setNode(node = 'https://testnode1.wavesnodes.com', chain = 'testnet')

try:    modal = sys.argv[1]
except: modal = "h"

#Help/Usage
if modal=="" or modal=="h" or modal=="-h" or modal=="help" or modal=="--help":
    print("")
    print("Glufco Investment")
    print("A brilliant python3: pywaves and cryptos implementation for")
    print("glufco/waves/bitcoin/litecoin/dash and other waves assets")
    print("")
    print("Commands usage:")
    print("balance      Get waves and glufco address balance")
    print("             args: address")
    print("newaddress   Create a new waves, bitcoin, litecoin or dash address")
    print("             with random or given seed")
    print("             args: coin=waves/bitcoin/litecoin/dash")
    print("                   seed=(optional)'a big long brainwallet password'")
    print("help         This help")
    print("sendglf      Send glufco from user1 to user2")
    print("             args: user1privKey - Sender private key")
    print("                   user2Address - Destination address")
    print("                   amount - Amount to send. Example: 100 for 1 glufco")
    print("                   message(optional)")
    print("             Transfer Fee = 0.1 glufco")
    print("sendwaves    Send waves from user1 to user2")
    print("             args: user1privKey - Sender private key")
    print("                   user2Address - Destination address")
    print("                   amount - Amount to send. Ex: 100000000 for 1 waves")
    print("             Transfer Fee = 0.001 waves")
    print("tx           Get transaction details")
    print("             args: coin=waves")
    print("                   txid")
    print("txcheck      Check if transaction is valid")
    print("             args: coin=waves")
    print("                   txid")
    print("validate     Validate address")
    print("             args: coin=waves")
    print("                   address") 
    print("version      Version")
    print("")

#Transaction check
if modal=="txcheck":
    if sys.argv[2]=="waves":
        v = pw.tx(sys.argv[3])
        try:
            if v['height']: print('true')
        except:
            print('false')

#Transaction details
if modal=="tx":
    if sys.argv[2]=="waves":
        v = pw.tx(sys.argv[3])
        print(v)

#Validate Address
if modal=="validate":
    if sys.argv[2]=="waves":
        v = pw.validateAddress(sys.argv[3])
        print(v)

#Version Address
if modal=="version":
    print(version)
    
#Address balance
# glufco: 3P4vfuBaH8aj7KCMKmBsUsu2F582zobuBBQ 
# admin : 3P5GTynzBaPozRemnkkQ2C9cRxf2bGJ4gtY
# DKBlu : 3P6hbyNmKjXKtvWH2uQTg54qr7a9CFDJ6fo
# pedro : 3P9rsoA1zFrNHTR1xKx6gF2Qqg7cKXazh8u
if modal=="balance":
    try:    
        address = pw.Address(sys.argv[2])
        WAVES = address.balance()
        GLUFCO = address.balance(assetId='FTWuoa82n61C8FkJwGkyRq2kMcbCptMmMnR4WpKvTD2c')
        data = {}
        data['network']='WAVES'
        data['address']= sys.argv[2]
        data['waves']= (str)(WAVES / 100000000.00)
        data['glufco']= (str)(GLUFCO / 100.00)
        datajson = json.dumps(data,ensure_ascii=False)
        print(datajson)
    except: 
        pass
    

#Create new waves address
if modal=="newaddress":
    try: cryptseed = sys.argv[3]
    except: cryptseed = entropy_to_words(os.urandom(16))
    if cryptseed=="": cryptseed = entropy_to_words(os.urandom(16))
    #cryptseed = 'a big long brainwallet password'
    
    if sys.argv[2]=="waves":
        myAddress = pw.Address(seed=cryptseed)
        data = {}
        data['network'] = 'WAVES'
        data['seed'] = myAddress.seed
        data['pvkey'] = myAddress.privateKey
        data['pbkey'] = myAddress.publicKey
        data['address'] = myAddress.address
        datajson = json.dumps(data,ensure_ascii=False)
        print(datajson)
    else:
        if sys.argv[2]=="bitcoin": 
            coin = Bitcoin()
            network = "BITCOIN"
        if sys.argv[2]=="litecoin": 
            coin = Litecoin()
            network = "LITECOIN"
        if sys.argv[2]=="dash": 
            coin = Dash()
            network = "DASH"
        data = {}
        data['network'] = network
        data['seed'] = cryptseed
        data['pvkey'] = sha256(cryptseed)
        data['pbkey'] = coin.privtopub(data['pvkey'])
        data['address'] = coin.pubtoaddr(data['pbkey'])
        datajson = json.dumps(data,ensure_ascii=False)
        print(datajson)


# Send waves from user1 to user2
"""A efectos de visualizacion:
El Balance de WAVES se divide entre 100000000.00 - 8 decimales
El Balance de TOKEN se divide entre 100.00 - 2 decimales
Pero siempre en las transacciones va a ir un numero entero desde el ultimo decimal"""
if modal=="sendwaves":
    user1privKey = sys.argv[2]
    user2address = sys.argv[3]
    amount = int(sys.argv[4]) #amount = 200000 > Send 0.002 waves
    user1 = pw.Address(privateKey = user1privKey)
    user2 = pw.Address(user2address)
    try:
        op = user1.sendWaves(recipient = user2, amount = amount)
        op1 = json.dumps(op, ensure_ascii=False)
        print (op1)
    except:
        print("ERROR")


# Send glufco from user1 to user2
if modal=="sendglf":
    user1privKey = sys.argv[2]
    user2address = sys.argv[3]
    amount = int(sys.argv[4]) #amount = 100 > Send 1 glufco
    try:
        message = sys.argv[5]
    except:
        message = ""
    user1 = pw.Address(privateKey = user1privKey)
    user2 = pw.Address(user2address)
    myToken = pw.Asset('FTWuoa82n61C8FkJwGkyRq2kMcbCptMmMnR4WpKvTD2c') 
    try:
        op = user1.sendAsset(recipient = user2, 
                            asset = myToken, 
                            amount = amount, 
                            feeAsset = myToken, 
                            txFee = 0.1, 
                            attachment = message)
        op1 = json.dumps(op, ensure_ascii=False)
        print(op1)
    except:
        print("ERROR")
