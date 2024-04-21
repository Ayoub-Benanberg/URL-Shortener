import pyshorteners

def shortner(url):
            shortLink = pyshorteners.Shortener()
            print(shortLink.tinyurl.short(url))
            
            
url = input ("Enter Votre URL : ")
shortner(url)
