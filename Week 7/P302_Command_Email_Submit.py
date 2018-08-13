#! python3
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if len(sys.argv) > 3:
    email = sys.argv[1]
    text = sys.argv[2]
else:
    print('Usage : Command [email] [text]')

browser = webdriver.Chrome(r'C:\Users\ChiHoon\Downloads\chromedriver\chromedriver.exe')
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('hcb0402')
IdNext = browser.find_element_by_id('identifierNext').click()
#passwordElem = browser.find_element_by_name('password')
passwordElem = browser.find_element_by_class_name('OabDMe cXrdqd Y2Zypf')
passwordElem.send_keys('djflq77clf!')
PasswordNext = browser.find_element_by_id('passwordNext').click()
