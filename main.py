import re
import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import xlsxwriter

head = {
    "cctcss": "square-cover",
    "cllayout":	"NORMAL",
    "clp":	"-gImCAESHAoWcmVjc190b3BpY182NFdqVzVubHFwRRA7GAMiBEdBTUU=:S:ANO1ljKTpeU",
    "ipf": "1",
    "num": "48",
    "numChildren":	"0",
   # "pagTok":	"gtP_uANOCkX6noGdAz8IkwEQ_J3WqgQQjML3wAkQrOTAwQ4QnsCMuQwQ6qekrAsQmOysxg4QqsfMkAMQr4bJiAsQn-2mhgkQ-oqT8AwQvpq2mJos:S:ANO1ljL-ueE",
    "pagtt":	"3",
    "start":	"144",
    "xhr":	"1"
}

page = "https://play.google.com/store/apps/collection/topselling_paid?hl=ru"

#browser = webdriver.Safari()
#browser.get(page)
#print(browser)
#browser.quit()
#r = requests.post(page, data=head)
with open('/Users/Yauheni/Desktop/page.txt', 'r') as read:
    page_ = read.read()
bsObj = BeautifulSoup(page_, "html.parser")

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', "Game")
worksheet.write('B1', "Factory")
worksheet.write('C1', "Suite")
worksheet.write('D1', "Email")


with open('games.txt', 'w') as output_file:

    suite = {}
    index = 1
    excel = 2
    nameList = bsObj.findAll("a", {"class": "title"})
    for i in nameList:
        print("Game: ", index)
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
            output_file.write(key + " - " + value + "\n")
            if key == "name":
                worksheet.write('A' + str(excel), value)
            elif key == "factory":
                worksheet.write('B' + str(excel), value)
            elif key == "suite":
                worksheet.write('C' + str(excel), value)
            else:
                worksheet.write('D' + str(excel), value)
        print()
        output_file.write("\n")
        index += 1
        excel += 1

#browser.quit()

