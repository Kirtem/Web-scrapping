import bs4
import requests
from fake_headers import Headers
from requests import get

if __name__ == "__main__":
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
base_url = 'https://habr.com'
url = base_url + '/ru/all'
response = requests.get(url, headers=header.generate())
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all("article")
article_list = soup.find_all('article', class_='tm-articles-list__item')

for article in article_list:
    date = article.find('time')
    title = article.find('h2', class_='tm-article-snippet__title')
    link = title.find('a', class_='tm-article-snippet__title-link')
    tags_element = article.find('div', class_='tm-article-snippet__hubs')
    tags = tags_element.findAll('span', class_='tm-article-snippet__hubs-item')
    tags = [tag.text.strip('* ') for tag in tags]
    text = article.find('div', class_='article-formatted-body').text
    for key_words in KEYWORDS:
        if key_words in title or key_words in tags or key_words in text:
            print(f'{date.text} - {title.text} - {base_url}{link.get("href")}')
