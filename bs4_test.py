import shutil
import tempfile
import urllib.request
import urllib.parse
import hashlib
import os
from bs4 import BeautifulSoup

# Get details and more from a secrets.py file
try:
    from secrets import url_list
except ImportError:
    print("Can't open the secrets file with the url_list")
    raise

def save_html(url, path):
    response = urllib.request.urlopen(url)
    c = response.read()
    with open(urlhash, 'wb') as f:
        f.write(c)


def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

for url in url_list:
    encoded = url.encode('utf-8')
    urlhash = hashlib.sha256(url.encode('utf-8')).hexdigest() + ".htm"

    if not os.path.exists(urlhash):
        print(f"Loading missing file {urlhash}")
        save_html(url, urlhash)
    page = str(open_html(urlhash))

    for i in range(3):
        tag="</TABLE>"
        endOfHeader = page.find(tag)
        index = endOfHeader
        print(f'{index}\n\n')
        ch = page[index+len(tag)+3:]
        page = ch

    soup = BeautifulSoup(page, 'html.parser')
    print(soup.prettify())

    # state machine for capturing story tags:
    # 1 - scan from beginning until the end of the second table (2nd /TABLE tag)
    # 2 - search for second <BR> tag
    # 3 - Loop around story tags... state machine:
    #     stories are delimited by blank lines...
    #       get <A> link tags to get the story link and title
    #       get text for the description, combine text from multiple lines until end 
    #           of story is found (double <BR>)
    #     end story link with <BR><BR>
    # 4 - story stops with multiple blank lines (>3)
