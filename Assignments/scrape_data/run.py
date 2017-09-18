# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:02:56 2017

@author: Lavanya Mengaraboina
"""
#This program shows the scraping of ICC rankings website. The information 
#for the top 100 batsman worldwide is being retrieved through this and is written 
#on to a CSV file.
#To download pages using the Python requests library.
import requests
import time
import random
#Container for the information to be scraped
top_players = []
#Open and write to file
f = open('output.csv','w+')
num = 100
#The website for scraping
url = "http://www.relianceiccrankings.com/alltime/test/" 
#Get requests from the respective url
request = requests.get(url).text.split('\n')
for line in request:
    #the line to be fetched to obtain the corresponding data
    fetch = line.find('href="/playerdisplay/Array')
    if fetch>0:
        line = line[fetch:]
        print(line)
        pos = line.find('">')
        f.write(line[pos+2: -9])
        f.write("\n")
        top_players.append(line[pos+2: -9])
num -= 1
time.sleep(random.randint(0, 3))    
print(top_players)
f.close()
