from bs4 import BeautifulSoup

class ObtencaoLinguagem:
    def __init__(self, html):
        self.html = html

    def get(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        table = soup.find('table', {'id': 'top20'})
        linguagens = []
        
        if table:
            for row in table.tbody.find_all('tr'):
                cols = row.find_all('td')
                if len(cols) >= 7:
                    linguagens.append({
                        'name': cols[4].get_text(strip=True),
                        'rating': cols[5].get_text(strip=True),
                        'change': cols[6].get_text(strip=True)
                    })
        return linguagens