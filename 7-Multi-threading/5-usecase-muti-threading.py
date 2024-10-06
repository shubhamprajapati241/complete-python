'''
Real-world Example : Multi-threading for I/O bound tasks

Scenarios : Web Scraping
Web-scraping often involves making numerrous network request to fetch web pages. These tasks are I/O bound because they spend a lot of time wating for responses for servers. Multi-threading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.
'''

'''
Web URLs: 
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/tutorials/

https://python.langchain.com/v0.2/docs/how_to/
'''
import threading
import requests
from bs4 import BeautifulSoup 

urls = [
   "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/tutorials/",
    "https://python.langchain.com/v0.2/docs/how_to/"
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters in {url}")
    # print(f'{soup.text}')

threads = []

for url in urls:
    thread  = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

## wait for all the thread to complete the execution
for thread in threads:
    thread.join()

print("printed all the pages")