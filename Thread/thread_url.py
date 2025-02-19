
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/how_to/pydantic_compatibility/',
]


def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'The url contaon {(len(soup.text))} words')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print('All web pages are fetched')