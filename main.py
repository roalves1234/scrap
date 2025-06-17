import requests
from Comum.Utils.utils import FileTool

url = "https://www.tiobe.com/tiobe-index/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    FileTool('response.html').save(response.text)
    print('Response salvo em response.html')
else:
    print(f"Erro: {response.status_code}")
