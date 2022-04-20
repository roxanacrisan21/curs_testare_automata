# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()
#
# navigam catre un url
chrome.get('https://www.phptravels.net')
sleep(2)

# selector by name
chrome.find_element(By.LINK_TEXT, 'Signup').click()

sleep(2)

# gasim mai multe si punem in lista
lista_formular = chrome.find_elements(By.TAG_NAME, 'input')
lista_formular[1].send_keys('Test')
lista_formular[2].send_keys('Abc')
lista_formular[3].send_keys('0756789012')
lista_formular[4].send_keys('test.abc@yahoo.ro')
lista_formular[5].send_keys('parolaMea!')
sleep(1)

select = Select(chrome.find_element(By.ID,'account_type')) # drop-down-list, il definim intr-o variabila
select.select_by_visible_text("Agent") # optiunea din drop-down-list pe care vreau sa o selectez
sleep(3)
chrome.quit()