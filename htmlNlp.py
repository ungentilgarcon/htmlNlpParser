#python3 code
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
url = "http://aadn.org/"
# //response = request.urlopen(url)
# //raw=  response.read().decode('utf8')
req = Request( url, headers={'User-Agent': 'Mozilla/5.0'})
# html = request.urlopen(url).read().decode('utf8')
html = urlopen(req).read().decode('utf8')
# print(response)
# print(raw)
# print (html)
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)
# print(tokens)
text = nltk.Text(tokens)
text.concordance('aadn')