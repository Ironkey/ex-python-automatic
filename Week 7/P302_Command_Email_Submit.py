#! python3
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if len(sys.argv) > 3:
    email = sys.argv[1]
    text = sys.argv[2]
else:
    print('Usage : Command [email] [text]')

browser = webdriver.Chrome(r'C:\Users\Parkchihoon\Downloads\chromedrive\chromedriver.exe')
browser.get('http://gmail.com')
htmlElem = browser.find_element_by_tag_name('html')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('hcb0402')
htmlElem.send_keys(Keys.ENTER)


passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('djflq77clf!')
passwordElem.submit()
