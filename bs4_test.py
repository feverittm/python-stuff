import shutil
import tempfile
import urllib.request
import urllib.parse
import hashlib
import os
import re
from bs4 import BeautifulSoup

# Get details and more from a secrets.py file
try:
    from secrets import url_list
except ImportError:
    print("Can't open the secrets file with the url_list")
    raise

def cache_html(url, path):
    encoded = url.encode('utf-8')
    urlhash=hashlib.sha256(encoded).hexdigest()
    with open(path, 'wb') as f:
        f.write(url)

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

def page_head(index, length):
    print(page[index + length])

def get_entry(address):
    link = address.attrs['href']
    print(f'Link = {link}')
    author_start = address.string.rfind('-')
    name = address.string[:author_start-1].strip()
    print(f'Story Title = {name}')

    author = address.string[author_start+1:].strip()
    p = re.compile('\s*by\s*')
    author = p.sub("",author)
    print(f'Author = {author}')

    description = address.next_sibling
    tag_start = description.rfind('(')
    story_tags = description[tag_start+1:-2].strip().replace(" ", "").split(',')
    description = description[:tag_start].strip()
    p = re.compile('^\s*-\s*')
    description = p.sub("",description)
    print(f'Description = {description}')
    print(f'Story Tags = {story_tags}')

    print("\n")



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
        print (page[:10])

    for i in range(2):
        tag="<BR>"
        endOfHeader = page.find(tag)
        index = endOfHeader
        print(f'{index}\n\n')
        ch = page[index+len(tag)+2:]
        page = ch
        print (page[:10])

    count=0
    soup = BeautifulSoup(page, 'html.parser')
    addresses = soup.find_all('a')
    for address in addresses:
        print(f'Count: {count}')
        get_entry(address)
        count = count + 1

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
