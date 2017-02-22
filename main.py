# coding=UTF-8

from bs4 import BeautifulSoup
import urllib2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("question_id", help="echo the string you use here")
parser.add_argument("question_num", help="echo the string you use here")
args = parser.parse_args()

print "<strong>" + args.question_id + ", 共 " + args.question_num  + " 題" + "</strong>"
question_id = args.question_id
question_num = args.question_num

url = "http://gre.kmf.com/question/" + question_id + ".html"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "html5lib")
mydiv = soup.find_all("div", class_="quecontent")
que = mydiv[0].find_all("div", class_="content")
print que[0].prettify().encode('utf-8')
print "<p></p>"
count = int(question_num)
for k in range(count):
    url = "http://gre.kmf.com/question/" + question_id + "-" + str(k + 1) + ".html"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html5lib")

    mydiv = soup.find_all("div", class_="options")
    opt = mydiv[0].find_all("div", class_="mb20")
    mystr = str(k + 1) + ". " + opt[0].prettify().encode('utf-8')
    print "<strong>" + mystr + "</strong>"
    choice = mydiv[0].find_all("ul", class_="sh-raido-options radio")
    for tag in mydiv[0].find_all('input'):
        tag.replaceWith('')

    if len(choice) == 0:
        choice = mydiv[0].find_all("ul", class_="sh-raido-options check")
    if len(choice) != 0:
        print choice[0].prettify().encode('utf-8')
