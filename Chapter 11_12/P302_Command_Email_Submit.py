#! python3
import sys, time
from selenium import webdriver

if len(sys.argv) > 3:
    email = sys.argv[1]
    text = sys.argv[2]

else:
    print('Usage : Command [email] [text]')

browser = webdriver.Chrome(r'C:\Users\ChiHoon\Downloads\chromedriver\chromedriver.exe')
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('id')
browser.find_element_by_id('identifierNext').click()
time.sleep(1)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('password')
browser.find_element_by_id('passwordNext').click()
time.sleep(1)
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(1)
browser.find_element_by_name('to').send_keys('test@test.com')
browser.find_element_by_name('subjectbox').send_keys('test')
browser.find_element_by_name('textbox').send_keys('testtest')