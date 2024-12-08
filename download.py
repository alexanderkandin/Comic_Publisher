import requests
import os



def download_image(url, save_path, payload=None):
    response = requests.get(url,params=payload) if payload else requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)