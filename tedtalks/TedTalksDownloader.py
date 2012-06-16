# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:00:40 2012

@author: kunj
"""
import urllib
from BeautifulSoup import BeautifulSoup
import sys
import os

def down_vid(first_num=None, num=None):
    url = "/".join(os.path.abspath(__file__).split("/")[:-1]+["html"]+["ted.html"])
    print url

    x=urllib.urlopen(url).read()
    soup=BeautifulSoup(x)

    hrefs = soup.findAll("a",{"target":True,"href":True,"style":True})

    try:	
        first_num = int(sys.argv[1])
        num = int(sys.argv[2])
    except IndexError:
        if not first_num or not num:
            print ("invalid")
            sys.exit()
    n=0
    for links in hrefs:
        if n < first_num:
            n+=1
            continue
        if n > first_num + num:
            break
        page_link = links.contents[0]
        page = urllib.urlopen(page_link).read()
        links = page.split()
        for link in links:
            if ".mp4" in link:
                url = link.split('"')[1]
                filename = url.split("/")[-1]
                try:
                    urllib.urlretrieve(url,os.path.join(os.getenv("HOME"),"Videos",filename))
                except:
                    print "unable to download", filename
                    n+=1
                    continue
                print filename, "saved"
                break
        n+=1
