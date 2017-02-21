# coding=UTF-8

from bs4 import BeautifulSoup
import urllib2

url = "http://gre.kmf.com/question/72b29j.html"

content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "html5lib")
#print soup.encode('utf-8')
#mydivs = soup.findAll('content')
mydiv = soup.find_all("div", class_="quecontent")
mydivs = mydiv[0].find_all("div", class_="content")
print mydivs[0].prettify().encode('utf-8')


mydiv = soup.find_all("div", class_="options")
mydivs = mydiv[0].find_all("div", class_="mb20")
print mydivs[0].prettify().encode('utf-8')

mydivs = mydiv[0].find_all("ul", class_="sh-raido-options radio")
print mydivs[0].prettify().encode('utf-8')
