import shutil
import tempfile
import urllib.request
import urllib.parse
import hashlib
from bs4 import BeautifulSoup

url_list = [ "http://www.asstr.org/~Kristen/inc/index1.htm" ]

def save_html(html, path):
    encoded = url.encode('utf-8')
    urlhash=hashlib.sha256(encoded).hexdigest()
    with open(path, 'wb') as f:
        f.write(html)


#print (f"url {url}, encoded {encoded}, hash {urlhash}")

#page = urlopen(url)

for url in url_list:
    encoded = url.encode('utf-8')
    urlhash=hashlib.sha256(url.encode('utf-8')).hexdigest()
    response = urllib.request.urlopen(url)
    c = response.read()
    print(c)
    with open(urlhash, 'wb') as f:
        f.write(c)

#with open(tmp_file.name) as page:
#    soup = BeautifulSoup(page, "html.parser")

#print(soup.get_text())
