#GPL V3
import sys
import urllib
from urllib.parse import urlparse


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
from urllib.request import FancyURLopener
import urllib3







#GETLINKS.PY

class FixFancyURLOpener(FancyURLopener):

    def http_error_default(self, url, fp, errcode, errmsg, headers):
        print(errcode)
        if errcode == 403:
            raise ValueError("403")
        return super(FixFancyURLOpener, self).http_error_default(
            url, fp, errcode, errmsg, headers

        )
        if errcode == 404:
            raise ValueError("404")
        return super(FixFancyURLOpener, self).http_error_default(
            url, fp, errcode, errmsg, headers
        
        )

# Monkey Patch
urllib.request.FancyURLopener = FixFancyURLOpener




# class MyOpener(urllib.request.FancyURLopener):
class MyOpener(FixFancyURLOpener):
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
        print(hrefReturn)
    return hrefReturn
# process(url)



#TRYING TO GO THE THREAD WAY 1/2 #NOT NOW ;)
def parse_text(url, table): 
# class parse_text(Thread):



    # def __init__(self,url, table): 

    #     Thread.__init__(self)

        # self.url = url
        # self.table = table #WHAT WAS IT FOR ALREADY? ;)
		print(url)
		# //response = request.urlopen(url)
		# //raw=  response.read().decode('utf8')
		# html = request.urlopen(url).read().decode('utf8')
		#GET TREE
		excludeList = ['pdf','PDF','doc','xls','zip','tar','ocx']
		urlLinked = processlinks(url)
		#AND LETS LOOP... 
		while urlLinked.__len__() < 999:
			
			for link in urlLinked:
				if any(x in link[-3:] for x in excludeList):
					continue
				print("link",link)
				print("url",url)
				parsed_uri1 = urllib.parse.urlparse( link )
				parsed_uri2 = urllib.parse.urlparse( url )
				domain1 ='{uri.netloc}'.format(uri=parsed_uri1)
				domain2 ='{uri.netloc}'.format(uri=parsed_uri2)
					#...BUT PROCESS ONLY IF URLS MATCH
				urlLinked2 = []
				urlIdent = []
				if domain1 == domain2 and parsed_uri1 != parsed_uri2:
					# try:
						try:
						    resp = urlopen(link)
						except urllib.error.URLError as e:
						    if not hasattr(e, "code"):
						        raise
						    resp = e

						print ("Gave", resp.code, resp.msg)
						print ("=" * 80)
						print (resp.read(80))
						urlLinked2 = processlinks(link)
						print("urlIdent",urlIdent)
						print("urlLinked",urlLinked)
						print("urlLinked2",urlLinked2)
						print("urlLinkedlength",urlLinked.__len__())
						print(set(urlLinked))
						urlIdent = set(urlLinked).intersection(urlLinked2)
						if urlIdent.__len__() > 0:
							urlLinked2.remove(urlIdent)
						if (urlLinked.__len__() + urlLinked2.__len__()) >= 999:
							break
						elif (urlLinked.__len__() + urlLinked2.__len__())< 999:
							urlLinked.append(urlLinked2)
							continue
						break
					# except ValueError:
					# 	print ("Oops!  That was no valid number.  Try again...")
				else:
					continue
			#SELECT ONLY THE NEW ONES,CHECK IF A THOUSAND OR MORE? IF NOT RERUN AND APPEND,IF SO THEN CUT AT 999....AND APPEND


		while urlLinked2.__len__() > (999 -urlLinked):
			urlLinked2.pop()
		urlLinked.append(urlLinked2)
		urlLinked.append(url)
		for urls in urlLinked:
			req = Request( urls, headers={'User-Agent': 'Mozilla/5.0'})
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

	for row in urlreader:
		parse_text(row[0],urlreader)
#TRYING TO GO THE THREAD WAY 2/2
	# Creation des threads
	thread_1 = Afficheur("1")
	thread_2 = Afficheur("2")

	# Lancement des threads
	thread_1.start()
	thread_2.start()

	# Attend que les threads se terminent
	thread_1.join()
	thread_2.join()



