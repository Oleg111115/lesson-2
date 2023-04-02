from bs4 import BeautifulSoup
import requests

url = "https://ru.wikipedia.org/wiki/Приозерск"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
paragraphs = []
remaining_content = []
remaining_content = soup.find_all()
for tag in remaining_content:
    if tag.find("p") is not None:
        paragraphs.append(tag.text)
for tag in paragraphs:

    print(tag)