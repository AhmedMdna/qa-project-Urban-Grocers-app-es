import configuration
import requests
import data

#Solicitud para obtener el token de un nuevo usuario
def get_new_user_token():
     new_user_token = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.USER_BODY,
                         headers = data.USER_HEADERS )

     return new_user_token.json().get("authToken") # Extrae el token de la respuesta


#Solicitud para crear un kit
def post_new_client_kit(name=None):  # Permitir name opcional
    auth_token = get_new_user_token()
    kit_headers = data.KIT_HEADERS.copy()
    kit_body = data.KIT_BODY.copy()
    kit_headers["Authorization"] = f"Bearer {auth_token}"

    if name is not None:  # Solo añade 'name' si se proporciona
        kit_body["name"] = name

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=kit_headers)