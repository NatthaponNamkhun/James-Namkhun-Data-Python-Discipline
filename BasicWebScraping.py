import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url = "https://inchenro.com/2024/03/26/everyone-can-do-just-learn-it/"

web_data = requests.get(url)
print(web_data.text)