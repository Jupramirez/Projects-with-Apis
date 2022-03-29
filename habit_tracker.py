import requests
from datetime import datetime


USERNAME = "pablo321"
TOKEN = "alfonsito321"

#Endpoint donde se encuentra el sistema
pixela_endpoint = "https://pixe.la/v1/users"
#Creacion del usuario
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Se realiza el requerimiento con los parametros en json
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Gym",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}
# se puede crear un header para evitar pasar por la url
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


today = datetime.now()

#Ahora para crear un pixel
pixel_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
#se agrega la configuracion
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.0"
}

# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)

#Actualizar con requests put
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220324"
pixel_update_config = {
    "quantity": "4.0"
}
# response = requests.put(url=pixel_update_endpoint,json=pixel_update_config,headers=headers)

#Delete a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220324"
response = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)