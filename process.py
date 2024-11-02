import json
import os.path
from random import randint
from time import sleep

from requests import get

with open('pdfs.json', 'r') as f:
    data = json.load(f)

pdfs = set()

for entry in data:
    pdfs.add(entry['pdf_url'])

print(f'Found {len(pdfs)} PDFs')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

for url in pdfs:
    filename = 'downloads/' + '_'.join(url.split('/')[-2:])
    if not os.path.isfile(filename):
        print(f'Downloading {url} to {filename}')
        try:
            r = get(url, headers=headers, stream=True)
            with open(f'{filename}', 'wb') as fd:
                for chunk in r.iter_content(1000):
                    fd.write(chunk)
            sleep(randint(1, 5))
        except Exception as e:
            print(f'Exception: {e}')
            sleep(randint(10, 30))
