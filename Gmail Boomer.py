import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    
    mensajes = [
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',
'PON LOS MENSAJES QUE QUIERAS AQUI',

   ]
    
    # Enviar cada mensaje de la lista
    for contenido in mensajes:
        try:
            # Crea un mensaje de correo
            message = MIMEText(contenido)
            message['to'] = 'COLOCA EL CORREO QUE QUIERES BOOMEAR'
            message['from'] = 'PON EL CORREO DESDE DONDE SE VA A ENVIAR'
            message['subject'] = 'Saludos'

            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            
            message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
            print(f'Message Id: {message["id"]} enviado exitosamente')
        except Exception as e:
            print(f"Error al enviar el correo: {e}")

if __name__ == '__main__':
    main()
