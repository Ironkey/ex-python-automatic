from selenium import webdriver

browser = webdriver.Chrome(r'C:\Users\ChiHoon\Downloads\chromedriver\chromedriver.exe')
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('hcb0402')
emailElem.submit()
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('12345')
passwordElem.submit()