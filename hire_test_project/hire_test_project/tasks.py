from celery import shared_task
import requests
from bs4 import BeautifulSoup as soup

@shared_task(bind=True, default_retry_delay=5)
def parse_html_page(self, url):
    # r = requests.get(url, timeout=(5,30))
    try:
        r = requests.get(url, timeout=(1,30))
    except requests.exceptions.ConnectionError as exc:
        raise self.retry(exc=exc, max_retries=5)
    s = soup(r.text, 'html.parser')
    res = {}
    for tag in ('a', 'h1', 'h2', 'h3'):
        res[tag] = len(s.find_all(tag))
    anchors = s.find_all('a', {'href': True})
    res['urls'] = [a['href'] for a in anchors if a['href']]
    return res