import re
import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
     'Cookie': "sessionId=.eJxNjU1qAkEQRs3EKI4M8WcnHiDZDJ4hrlR0Ida6qekusHHSMz1VbTAQcCV4H_FAniQIKu4ej-_x7aM___IBXSZmW7iSKrYs5OQIyc0pFqxkVoNEYZC1CkyVsmZ6Ovdr8H4fkcMsJzOLoI5szQLaUrAKpUEh46Mj9J7qDPWGnIHRD2XoMN-J1Zyi1kVwko6RaeKYHFuxW5oXhvKvW9HBnCpRek16o8R-k74eXCF-gH-FuHmJkn4ybE0HutzJb6xgNY59_XPp3w5L3wjpPy3BWVQ:1elg1A:Gq9X29CTUbzJLKymaQ5BLthk58c; csrftoken=KcUQHLdzAJN7f60K8WGpkV9lcq1pK1Yt; _ga=GA1.2.368121439.1518548367; _gid=GA1.2.528004347.1518548367; wcs_bt=s_14249a956b4d:1518549286; _hp2_ses_props.3646280627=%7B%22ts%22%3A1518548368060%2C%22d%22%3A%22www.appannie.com%22%2C%22h%22%3A%22%2Faccount%2Flogin%2F%22%7D; _hp2_id.3646280627=%7B%22userId%22%3Anull%2C%22pageviewId%22%3A%222763479085575662%22%2C%22sessionId%22%3A%228134842313275049%22%2C%22identity%22%3A%221291956%22%2C%22trackerVersion%22%3A%223.0%22%7D; usbls=1; _mkto_trk=id:071-QED-284&token:_mch-appannie.com-1518548371157-96208; _tdim=de04567c-346f-4482-8062-be68864bca86; aa_user_token=.eJxrYKotZNQI5SxNLqmIz0gszihkClWwsDQ1MzY0NDZKS7W0MDY1TDQ0NbUwN0g2M7Y0MDAzSwoVik8sLcmILy1OLYpPSkzOTs1LKWQONShPTUrMS8ypLMlMLtZLTE7OL80r0XNOLE71zCtOzSvOLMksS_XNT0nNcYLqYQnlRTIpM6WQ1WvLNmGGUj0ALiAy3Q:1elg1A:SCArzrlp9Wym-RrO9PqTGdbbn5k; rid=0a201d1e0fa7459a8d7aa8dd13e94691; _gat_UA-2339266-6=1"
}


page = "https://play.google.com/store/apps/collection/topselling_paid?hl=ru"

browser = webdriver.Safari()
browser.get(page)
r = browser.page_source
bsObj = BeautifulSoup(r, "html.parser")

with open('test.html', 'w') as output_file:
  output_file.write(r)

suite = {}

nameList = bsObj.findAll("a", {"class": "title"})
for i in nameList:
    new = BeautifulSoup((requests.get("https://play.google.com" + i['href'])).text, "html.parser")
    n = new.findAll("div", {"class": "id-app-title"})
    suite['name'] = (n[0]).text
    n = new.findAll("span", {"itemprop": "name"})
    suite['factory'] = (n[0]).text
    n = new.findAll("a", {"class": "dev-link"})
    suite['suite'] = (n[0])['href']
    try:
        suite['email'] = (n[1])['href']
    except IndexError:
        suite['email'] = 'NONE'
    for key, value in suite.items():
        print(key, " - ", value)
    print()

browser.quit()