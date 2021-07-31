"""class UrlShortener(object):
    def __init__(self):
       self.original_url = ""

    def getOriginalURL(self):
        original_url = raw_input('Enter the url:')
        print(original_url)



user = UrlShortener()
user.getOriginalURL() """

import pyshorteners
import sys
url = input("Enter the url:")
shortener = pyshorteners.Shortener()
shortened_url = shortener.tinyurl.short(url)
print("The Shortened URL is:",shortened_url)
input=sys.argv[1]
print(input)






        