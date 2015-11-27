#GPL V3
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
from threading import Thread
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
    hrefReturn = []
    for tag in soup.findAll('a', href=True):
        tag['href'] = urllib.parse.urljoin(url, tag['href'])
        hrefReturn.append(tag['href'])
        # print(hrefReturn)
    return hrefReturn
# process(url)



#TRYING TO GO THE THREAD WAY 1/2
#def parse_text(url, table): 
class parse_text(Thread):



    def __init__(self,url, table): 

        Thread.__init__(self)

        self.url = url
        self.table = table
		print(url)
		# //response = request.urlopen(url)
		# //raw=  response.read().decode('utf8')
		# html = request.urlopen(url).read().decode('utf8')
		#GET TREE
		urllinked = processlinks(url)
		#AND LETS LOOP... 
		for link in urllinked:
			parsed_uri1 = urlparse( link )
			parsed_uri2 = urlparse( url )
			domain1 ='{uri.netloc}'.format(uri=parsed_uri1)
			domain2 ='{uri.netloc}'.format(uri=parsed_uri2)
				#...BUT PROCESS ONLY IF URLS MATCH
			if domain1 == domain2:
				urllinked2 = processlinks(link)
		#CHECK IF A THOUSAND OR MORE? IF NOT RERUN,IF SO CUT AT 999....AND APPEND

	urllinked.append(url)
	req = Request( url, headers={'User-Agent': 'Mozilla/5.0'})
	html = urlopen(req).read()#.decode('utf8')
	raw = BeautifulSoup(html, "html5lib").get_text()
		#FOR TESTING IF NEEDED
		# print(response)
		# print(raw)
		# print (html)




#THE NLTK PART,BETTER FITTED SOMEWHERE ELSE
	tokens = word_tokenize(raw)
	# print(tokens)
	text = nltk.Text(tokens)
	with open('./data/liste_sigles.csv', newline='') as csvfile:
		siglereader=csv.reader(csvfile, delimiter=',', quotechar='|')
		#SKIP HEADER
		next(siglereader, None) 
		for row in siglereader:
			print (url,">>>>>>>>>>",row[0])
			text.concordance(row[0])









with open('./data/liste_sites.csv', newline='') as csvfile:
	urlreader=csv.reader(csvfile, delimiter=',', quotechar='|')
	#SKIP HEADER
	next(urlreader, None) 

	#for row in urlreader:
	#	parse_text(row[0],urlreader)
#TRYING TO GO THE THREAD WAY 2/2
	# Création des threads
	thread_1 = Afficheur("1")
	thread_2 = Afficheur("2")

	# Lancement des threads
	thread_1.start()
	thread_2.start()

	# Attend que les threads se terminent
	thread_1.join()
	thread_2.join()



