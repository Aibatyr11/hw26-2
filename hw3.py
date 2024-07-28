import requests
url = 'https://yandex.kz/pogoda/ru-KZ/astana/date/july/1' 

response = requests.get(url)
response.raise_for_status()
html_content = response.text

lines = html_content.split('\n')

temp = None  

for line in lines:
    if 'Temp:' in line:
        parts = line.split(' ')
        for part in parts:
            if part.endswith('°C'):
                temp = part
                break


print(f"{temp}")

