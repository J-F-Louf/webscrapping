# import libraries
import urllib
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.nature.com/nature/volumes/561/issues/7721'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

#Grab 'Research' (parent of Articles and letters)
name_parent = soup.find('div', attrs={'id':'Research-content'})

#we go one in because ext element is a 'ul', ul = unordered list, li=list item, h=headings it's the level
children = name_parent.findChildren('ul', recursive=False)
for child in children:
    list_items = child.findChildren(['h3', 'li'], recursive=False)
    for item in list_items:
        if (item.getText().strip()=='Articles'):
            break
        item.decompose()
    #we use 'with' so the file automatically closes after writting is done
    with open('output.txt','w+') as file:
        file.write(str(list_items))

# Find article categorie
#name_box = soup.find('h3', string='Articles')
