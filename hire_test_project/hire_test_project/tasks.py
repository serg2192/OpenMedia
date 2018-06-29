from celery import shared_task
import requests
from bs4 import BeautifulSoup as soup

@shared_task(bind=True, default_retry_delay=5)
def parse_html_page(self, url):
    try:
        r = requests.get(url, timeout=(1,30))
    except requests.exceptions.ConnectionError as exc:
        raise self.retry(exc=exc, max_retries=5)
    s = soup(r.text, 'html.parser')
    res = {}
    for tag in ('a', 'h1', 'h2', 'h3'):
        tags = s.find_all(tag)
        if tag == 'a':
            res['urls'] = [a['href'] for a in tags if a.get('href', None)]
        #     hrefs = []
        #     c = 0
        #     for a in tags:
        #         c += 1
        #         href = a.get('href', None)
        #         if href:
        #             hrefs.append(href)
        #     res[tag] = c
        #     res['urls'] = hrefs
        # else:
        #     res[tag] = len(tags)
        res[tag] = len(tags)
    return res