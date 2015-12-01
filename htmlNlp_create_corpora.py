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
from subprocess import call



with open('./data/liste_sites.csv', newline='') as csvfile:
    urlreader=csv.reader(csvfile, delimiter=',', quotechar='|')
    #SKIP HEADER
    next(urlreader, None) 

    for row in urlreader:
        argO = (row[0])
        print(argO, "\n")
        call(['/usr/bin/perl', './httrackSiteDownloader.pl',  "{}".format(argO)])

