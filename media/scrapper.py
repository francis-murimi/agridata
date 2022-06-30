import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import nltk

url = 'https://www.businessdailyafrica.com/bd/corporate/companies/equity-bank-excites-its-staff-with-fresh-share-reward-3863976'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print( 'hello world')
decoded_string = urlopen(req).read().decode() # convert bytes to str
my_text = BeautifulSoup(decoded_string,features="lxml").get_text() # get the text from html and javascript
print( 'hello world')
my_text.encode(encoding = 'UTF-8', errors = 'replace') # use UTF-8 encoding.
sent_list = nltk.tokenize.sent_tokenize(my_text) # split text into sentences
print( 'hello world')
content = sent_list[3:-10] # get the sentences that are commonly unique for each post
content = ''.join(s for s in content) # combine the sentences
print( 'hello world')
# separate and join lines to form paragraphs
lines = content.split("\n")
non_empty_lines = [line for line in lines if line.strip() != ""]
clean_content = ""
print( 'hello world')
for line in non_empty_lines:
    clean_content += line + "\n"
    
print(my_text) 


