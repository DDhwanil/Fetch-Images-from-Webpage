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
soup = BeautifulSoup(page)
soup.find_all('img src')
soup.find_all("title")
dir=str(subprocess.check_output(["pwd"])).rstrip('\n')
dir=dir+'/images'
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
