# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3  2017

@author: tpwin10

designed to work on one page of google search results for 'cnn'


"""


from bs4 import BeautifulSoup
import requests

#currently you must manually change articleoutput number if you dont want to
#overwrite previous output
path = r'C:\Users\tpwin10\.spyder-py3\articleOutput13.txt'

newFile = open(path, 'w', encoding="utf-8")

#currently you must manually paste in the google search result URL
r = requests.get("https://www.google.com/search?q=cnn&client=opera&biw=958&bih=940&tbm=nws&ei=gEiVWPWmHcm3mwGN85aABQ&start=130&sa=N&dpr=1")

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")

counter = 0

fixedLink = []

for link in links:
    if "http" in link.get("href"):
        if "cnn.com" in link.get("href"): 
            counter += 1
            print(counter)
            print(link.get("href")[7:])
            if counter % 2 == 0:
                fixedLink.append(link.get("href")[7:])
        
for link in fixedLink:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    soup.encode("ascii")
    print("%%%%%%%%%NEW STORY%%%%%%)")
    newFile.write(link + "\n")
    for titl in soup.find_all("h1"):
        newFile.write(titl.text + "\n")
    for para in soup.find_all("p"):
        newFile.write(para.text)
    for para in soup.find_all("div", class_="zn-body__paragraph"):
        newFile.write(para.text + "\n")

newFile.close()