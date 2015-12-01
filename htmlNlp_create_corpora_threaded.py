#GPL V3
import sys
import urllib
from urllib.parse import urlparse

import threading
import queue
import traceback
import threadpool
import time

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



    # the work the threads will have to do (rather trivial in our example)
def catchThis(argO):

    print(argO, "\n")
    call(['/usr/bin/perl', './httrackSiteDownloader.pl',  "{}".format(argO)])



with open('./data/liste_sites.csv', newline='') as csvfile:
    urlreader=csv.reader(csvfile, delimiter=',', quotechar='|')
    #SKIP HEADER
    next(urlreader, None) 
    data = [row[0] for row in urlreader]

    # assemble the arguments for each job to a list...
    # ... and build a WorkRequest object for each item in data

    requests = threadpool.makeRequests(catchThis, data)


    # we create a pool of 5 worker threads
    print("Creating thread pool with 5 worker threads.")
    main = threadpool.ThreadPool(5)

    # then we put the work requests in the queue...
    for req in requests:
        main.putRequest(req)
        print("Work request #%s added." % req.requestID)
    # or shorter:
    # [main.putRequest(req) for req in requests]

    # ...and wait for the results to arrive in the result queue
    # by using ThreadPool.wait(). This would block until results for
    # all work requests have arrived:
    # main.wait()

    # instead we can poll for results while doing something else:
    i = 0
    while True:
        try:
            time.sleep(0.5)
            main.poll()
            print("Main thread working...", end=' ')
            print("(active worker threads: %i)" % (threading.activeCount()-1, ))
            if i == 10:
                print("**** Adding 3 more worker threads...")
                main.createWorkers(3)
            if i == 20:
                print("**** Dismissing 2 worker threads...")
                main.dismissWorkers(2)
            i += 1
        except KeyboardInterrupt:
            print("**** Interrupted!")
            break

    if main.dismissedWorkers:
        print("Joining all dismissed worker threads...")
