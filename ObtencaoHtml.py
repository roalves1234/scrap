import requests
import os
from Comum.Utils.utils import FileTool

class ObtencaoHtml:
    def __init__(self):
        self.url = "https://www.tiobe.com/tiobe-index/"
        self.output_file = "response.html"
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def get_from_url(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            FileTool(self.output_file).save(response.text)
            return response.text
        else:
            raise Exception(f"Falha ao tentar abrir {self.url}. Status code: {response.status_code}")

    def get(self):
        if os.path.exists(self.output_file):
          return FileTool(self.output_file).load()
        else:
          return self.get_from_url()
