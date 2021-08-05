import shutil
import tempfile
import urllib.request
import urllib.parse
import hashlib
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"

def cache_html(url, path):
    encoded = url.encode('utf-8')
    urlhash=hashlib.sha256(encoded).hexdigest()
    with open(path, 'wb') as f:
        f.write(url)


#print (f"url {url}, encoded {encoded}, hash {urlhash}")

#page = urlopen(url)

encoded = url.encode('utf-8')
urlhash=hashlib.sha256(url.encode('utf-8')).hexdigest()
with urllib.request.urlopen(url) as response:
    c = response.read()
    print(c)
    with open(urlhash, 'wb') as f:
        f.write(c)
    #with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    #    shutil.copyfileobj(response, urlhash)


#with open(tmp_file.name) as page:
#    soup = BeautifulSoup(page, "html.parser")

#print(soup.get_text())
