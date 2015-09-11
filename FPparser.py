
from bs4 import BeautifulSoup
import requests

def bs4_test():
    url = 'http://www.fantasypros.com/experts/john-paulsen.php#accuracy'

    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    ranks = soup.find_all('tr')


    for item in ranks:
        print(item)



bs4_test()

