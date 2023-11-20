import requests

wine_url = "https://upload.wikimedia.org/wikipedia/commons/0/01/L%C3%ADnea_6_V%C3%ADa_Austral_Punta_Arenas.png"
response = requests.get(wine_url, stream=True)
print("Content-Type:", response.headers.get('Content-Type'))
