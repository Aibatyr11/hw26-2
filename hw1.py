import requests
import os
import random

def download_random_image(url, img):
    response = requests.get(url)
    response.raise_for_status()  
    file_name = os.path.join(img, f'image_{random.randint(1, 10)}.jpg')

    with open(file_name, 'wb') as file:
        file.write(response.content)   
    print(f"Изображение сохранено как {file_name}")


img = 'images'
os.makedirs(img, exist_ok=True)

base_url = 'https://wallpapers.com/nature#google_vignette'

for _ in range(10):
    download_random_image(base_url, img)
