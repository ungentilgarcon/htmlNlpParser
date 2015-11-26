import sys
import urllib
from urllib import parse


#python3 code
import csv
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import re



#GETLINKS.PY

class MyOpener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


def processlinks(url):
    myopener = MyOpener()
    #page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    for tag in soup.findAll('a', href=True):
        tag['href'] = urllib.parse.urljoin(url, tag['href'])
        print (tag['href'])
# process(url)




def parse_text(url, table): 
	print(url)
	# //response = request.urlopen(url)
	# //raw=  response.read().decode('utf8')
	req = Request( url, headers={'User-Agent': 'Mozilla/5.0'})
	# html = request.urlopen(url).read().decode('utf8')
	html = urlopen(req).read()#.decode('utf8')
	#FOR TESTING IF NEEDED
	# print(response)
	# print(raw)
	# print (html)
	#GET TREE
	processlinks(url)
	raw = BeautifulSoup(html, "html5lib").get_text()
	tokens = word_tokenize(raw)
	# print(tokens)
	text = nltk.Text(tokens)
	with open('./data/liste_sigles.csv', newline='') as csvfile:
		siglereader=csv.reader(csvfile, delimiter=',', quotechar='|')
		next(siglereader, None) 
		for row in siglereader:
			print (url,">>>>>>>>>>",row[0])
			text.concordance(row[0])









with open('./data/liste_sites.csv', newline='') as csvfile:
	urlreader=csv.reader(csvfile, delimiter=',', quotechar='|')
	next(urlreader, None) 

	for row in urlreader:
		parse_text(row[0],urlreader)




