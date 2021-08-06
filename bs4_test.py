import shutil
import tempfile
import urllib.request
import urllib.parse
import hashlib
import os
from bs4 import BeautifulSoup

url_list = [ "http://www.asstr.org/~Kristen/inc/index1.htm" ]

def save_html(url, path):
    response = urllib.request.urlopen(url)
    c = response.read()
    with open(urlhash, 'wb') as f:
        f.write(c)

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

#print (f"url {url}, encoded {encoded}, hash {urlhash}")

#page = urlopen(url)

for url in url_list:
    encoded = url.encode('utf-8')
    urlhash=hashlib.sha256(url.encode('utf-8')).hexdigest()

    if not os.path.exists(urlhash):
        print(f"Loading missing file {urlhash}")
        save_html(url, urlhash)
    page = open_html(urlhash)
    soup = BeautifulSoup(page, "html.parser")

    rows = soup.select('a')

    for i in range(len(rows)):
        print(f'row {i}: {rows[i]}')