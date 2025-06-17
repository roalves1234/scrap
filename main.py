import requests

url = "https://www.tiobe.com/tiobe-index/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.text)  
else:
    print(f"Erro: {response.status_code}")
