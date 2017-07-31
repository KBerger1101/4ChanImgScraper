#4ChanImageScraper

from bs4 import BeautifulSoup, SoupStrainer

import requests
import re
import urllib
import shutil


url = "4chan.org/co/"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data,'html.parser')


#pick out all of the image file from the html code
images = soup.find_all(class_='fileThumb')
imageCount=0
#go through them individually
for image in images:
    
    print(imageCount)
    urlimage= str(image)
    match=re.findall( r'href="([^"]*)"' ,urlimage)
    #ignore the error images
    if imageCount>1:
        
        urlimage = match[0] 
        print(urlimage)
        
        imageSiteUrl= "http:" +urlimage
        response = requests.get(imageSiteUrl, stream=True)
        with open('img'+str(imageCount)+'.png','wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    imageCount+=1

print("You wish has been granted")



