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






pagesScraped = 90
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
    if "#" not in url:

        page = myopener.open(url)
        excludeList = ['pdf','PDF','doc','xls','zip','tar','ocx','gif','GIF','svg','SVG','mp3','MP3','flv']
        print("url", url)
        text = page.read()
        page.close()

        soup = BeautifulSoup(text)
        hrefReturn = []
        for tag in soup.findAll('a', href=True):
            tag['href'] = urllib.parse.urljoin(url, tag['href'])
            #WE NEED TO ASSURE NOT A FILE OF SOME SORT
            if any(x in tag['href'][-3:] for x in excludeList):
                        continue
            #WE NEED TO GET RID OF ADDRESSES
            if "@" not in tag['href'] and "mailto" not in tag['href']:
            #WE NEED TO GET RID OF THE 404,403 and such ERRORS
                try:
                    resp = urlopen(tag['href'])
                except urllib.error.URLError as e:
                        if not hasattr(e, "code"):
                            raise
                        resp = e
                #FOR TESTING
                print ("Gave", resp.code, resp.msg)
                print ("=" * 80)
                print (resp.read(80))
                hrefReturn.append(tag['href'])
                print(hrefReturn)
        return hrefReturn
    # process(url)



#TRYING TO GO THE THREAD WAY 1/2 ##NOT NOW ;)
def parse_text(url, table): 
# class parse_text(Thread):



    # def __init__(self,url, table): 

    #     Thread.__init__(self)

        # self.url = url
        # self.table = table #WHAT WAS IT FOR ALREADY? ;)
        # //response = request.urlopen(url)
        # //raw=  response.read().decode('utf8')
        # html = request.urlopen(url).read().decode('utf8')
        
        #GET TREE
        print(url)
        excludeList = ['pdf','PDF','doc','xls','zip','tar','ocx','gif','GIF','svg','SVG','mp3','MP3','flv']
        urlLinked = processlinks(url)
        #AND LETS LOOP... 
        while urlLinked.__len__() < pagesScraped:
            
            for link in urlLinked:
                if any(x in link[-3:] for x in excludeList):
                    continue
                #WE COMPARE THE URL NETLOC TO SEE IF THEY MATCH (CAUSE IF NOT WE ARE OUTSIDE OF DOMAIN, SO NOT ON THE SITE)
                print("link",link)
                print("url",url)
                parsed_uri1 = urllib.parse.urlparse( link )
                parsed_uri2 = urllib.parse.urlparse( url )
                domain1 ='{uri.netloc}'.format(uri=parsed_uri1)
                domain2 ='{uri.netloc}'.format(uri=parsed_uri2)
                    #...WE PROCESS ONLY IF URLS MATCH...
                urlLinked2 = []
                urlIdent = []
                #BUT NOT IF THEY ARE EXACTLY THE SAME
                if domain1 == domain2 and parsed_uri1 != parsed_uri2:
                    # WE NEED TO GET RID OF ERRORS FIRST
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        urlLinked2 = processlinks(link)
                        print("urlLinked",urlLinked)
                        print("urlLinked2",urlLinked2)
                        print("urlLinkedlength",urlLinked.__len__())
                        print(set(urlLinked))
                        if urlLinked2 is not None:
                            print(set(urlLinked2))
                            urlIdent = set(urlLinked).intersection(urlLinked2)
                            print("urlIdent",urlIdent)
                            if urlIdent.__len__() > 0:
                                for urlI in urlIdent:
                                    urlLinked2.remove(urlI)
                            if (urlLinked.__len__() + urlLinked2.__len__()) >= pagesScraped:
                                while urlLinked2.__len__() > (pagesScraped - urlLinked.__len__()):
                                    #TRIM THE EXTRA URLs 
                                    urlLinked2.pop()
                                urlLinked.append(urlLinked2)
                                urlLinked.append(url)
                                break
                            elif (urlLinked.__len__() + urlLinked2.__len__())< pagesScraped:
                                urlLinked.append(urlLinked2)
                                continue
                            break
                    # except ValueError:
                    #   print ("Oops!  That was no valid url.  Try again...")
                else:
                    continue
            #SELECT ONLY THE NEW ONES,CHECK IF A THOUSAND OR MORE? IF NOT RERUN AND APPEND,IF SO THEN CUT AT pagesScraped9....AND APPEND


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

    # Creation des threads ###TODO
    # thread_1 = Afficheur("1")
    # thread_2 = Afficheur("2")

    # # Lancement des threads
    # thread_1.start()
    # thread_2.start()

    # # Attend que les threads se terminent
    # thread_1.join()
    # thread_2.join()



