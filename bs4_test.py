import shutil
import tempfile
import urllib.request
import urllib.parse
import hashlib
import os
import re
import pprint
import json
import sys
import ssl
from bs4 import BeautifulSoup

# Get details and more from a secrets.py file
try:
    from my_secrets import url_list
except ImportError:
    print("Can't open the secrets file with the url_list")
    raise

def cache_html(url, path):
    ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
    #print(f'path ... {path}')
    with open(path, 'wb') as f:
        with urllib.request.urlopen(url) as response:
            f.write(response.read())

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

def page_head(index, length):
    print(page[index + length])

def get_entry(address):
    """
    Data structure for entry:
    """
    entry = {}

    link = address.attrs['href']
    if link[:4] == 'index':
        return()
    print(f'Link = {link}')
    print(f'   address string: {address.string.strip()}')
    if address.string.strip()[:5] == 'Part ':
        story_part = address.string[5:]
        name = stories[-1]['name']
        print(f"   ... multipart story {story_part}")
        if name[len(name)-6:-1] == 'Part ':
            name = name[:-1] + story_part
        else:
            name = name + ' - Part ' + story_part
        print (f'    ... multipart story title: {name}')
        author = stories[-1]['author']
        description = stories[-1]['description']
        story_tags = stories[-1]['tags']
        #if int(story_part) > 4:
        #    sys.exit()

    else:
        author_start = address.string.rfind('-')
        name = address.string[:author_start-1].strip()
        author = address.string[author_start+1:].strip()
        p = re.compile('\s*by\s*')
        author = p.sub("",author)
        description = address.next_sibling
        tag_start = description.rfind('(')
        tag_end = description.rfind(')')
        print(f'  start tag search from right side: {tag_start} to {tag_end}')
        # capture the description skipping the starting <B> tag... and capture until 
        #   the opening '(' of the ending story tag
        story_tags = description[tag_start+1:tag_end].strip().replace(" ", "").split(',')
        description = description[:tag_start].strip()
        p = re.compile('^\s*-\s*')
        description = p.sub("",description)

    print(f'Story Title = {name}')
    print(f'Author = {author}')
    print(f'Description = {description}')
    print(f'Story Tags = {story_tags}')
    print("\n")

    entry['link'] = link
    entry['name'] = name
    entry['author'] = author
    entry['description'] = description
    entry['tags'] = story_tags
    stories.append(entry) 
 

def main():
    for url in url_list:
        urlhash = hashlib.sha256(url.encode('utf-8')).hexdigest() + ".htm"

        print(f'Loading url {url} ...')

        if not os.path.exists(urlhash):
            print(f"Loading missing file {url}")
            cache_html(url, urlhash)
        page = str(open_html(urlhash))

        for i in range(3):
            tag="</TABLE>"
            endOfHeader = page.find(tag)
            index = endOfHeader
            #print(f'{index}\n\n')
            ch = page[index+len(tag)+3:]
            page = ch
            #print (page[:10])

        for i in range(2):
            tag="<BR>"
            endOfHeader = page.find(tag)
            index = endOfHeader
            #print(f'{index}\n\n')
            ch = page[index+len(tag)+2:]
            page = ch
            #print (page[:10])

        count=0
        soup = BeautifulSoup(page, 'html.parser')
        addresses = soup.find_all('a')
        for address in addresses:
            print(f'Count: {count}')
            link = address.attrs['href']
            if link[:5] == 'index':
                break
            #print (f'  ... link = {link[:5]}')
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

if __name__ == "__main__":
    stories = []
    main()
    
    with open('stories.json', 'w') as outfile:
        json.dump(stories, outfile)
