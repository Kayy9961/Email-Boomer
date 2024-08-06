Paso 1: Crear un Proyecto en Google Cloud Console
Accede a Google Cloud Console:

Visita Google Cloud Console.
Inicia sesión con tu cuenta de Google si no lo has hecho ya.
Crear un nuevo proyecto:

Haz clic en el menú desplegable del selector de proyecto en la parte superior de la página.
Selecciona "Nuevo proyecto".
Asigna un nombre a tu proyecto y haz clic en "Crear".

Paso 2: Habilitar la API de Gmail
Habilita la API de Gmail:
Con el proyecto seleccionado, ve al menú de navegación y selecciona "API y servicios" > "Biblioteca".
Busca "Gmail API" en la barra de búsqueda.
Haz clic en "Gmail API" y luego en "Habilitar".

Paso 3: Configurar la Pantalla de Consentimiento de OAuth
Configura la pantalla de consentimiento:
En "API y servicios", selecciona "Pantalla de consentimiento OAuth".
Elige "Externa" si solo estás probando o desarrollando, o "Interna" si el proyecto es para uso organizacional.
Completa la información requerida, como el nombre de la aplicación, correo electrónico de soporte, y cualquier otra información necesaria.
Guarda los cambios.

Paso 4: Crear Credenciales de OAuth2
Crear credenciales:
En "API y servicios", selecciona "Credenciales".
Haz clic en "Crear credenciales" y elige "ID de cliente de OAuth".
Configura el tipo de aplicación como "Aplicación de escritorio" si estás probando desde una aplicación local.
Descarga el archivo JSON de credenciales que contiene el client_id y client_secret.

Paso 5: Añadir Cuentas de Prueba
Agregar usuarios de prueba:
En la configuración de la pantalla de consentimiento OAuth, desplázate hacia abajo hasta "Usuarios de prueba".
Agrega las cuentas de correo electrónico que usarás para probar la aplicación.


Instala las bibliotecas necesarias:

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
