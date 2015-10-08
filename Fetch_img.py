from bs4 import BeautifulSoup
import urllib2
import os
from annobrowser import *
import subprocess


ab=annobrowser()
ab.anonymize()
url=raw_input('Enter url :http://')
url='http://'+url
page=ab.open(url).read()
o=raw_input('Enter 1 for Windows os and 2 for Linux :')
if o=='1':
    dir=raw_input('Enter location to write images :')
if o=='2':
    print '\n\n Directory\n',
    dir=str(subprocess.check_output(["pwd"])).rstrip('\n')
    dir=dir+'/images'
    print dir

soup = BeautifulSoup(page)
soup.find_all('img src')
soup.find_all("title")


print soup.a
print soup.title
for link in soup.find_all('img'):

    filename=link['src'].lstrip('http://')
    filename=os.path.join(dir,filename.replace('/','_'))
    print filename
    data=ab.open(link['src']).read()
    ab.back()
    save=open(filename,'wb')
    save.write(data)
    save.close()
