from selenium import webdriver

browser = webdriver.Chrome(r'C:\Users\ChiHoon\Downloads\chromedriver\chromedriver.exe')
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Automate the Boring Stuff with Python')
type(linkElem)
linkElem.click()