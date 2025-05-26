#Request Headers
USER_HEADERS = {
    "Content-Type": "application/json"
}

KIT_HEADERS = {
    "Content-Type": "application/json",
    # "Authorization" se añadirá dinámicamente después de obtener el token
}

#Request bodies
KIT_BODY = {
    "userId": 1,
    #"name": "A"  # Campo a probar se añadirá dinamicamente con la función
    }

USER_BODY = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}