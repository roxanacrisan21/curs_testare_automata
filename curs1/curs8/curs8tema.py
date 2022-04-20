from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # descarcare chrome
from selenium.webdriver.common.by import By # pt accesarea elementelor din interfata

# # initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# # navigam catre un url
# chrome.get('http://automationpractice.com/index.php')
# sleep(3)
#
# # selector by ID/NAME

# search = chrome.find_element(By.ID, 'search_query_top')
# search.send_keys('Dress')
# sleep(3)
# chrome.find_element(By.NAME, 'submit_search').click()
# sleep(5)
# chrome.find_element(By.ID, 'contact-link').click()
# sleep(7)
# chrome.find_element(By.ID, 'email').send_keys('roxana@crisan')
# sleep(3)
# chrome.find_element(By.NAME, 'id_order').send_keys('2255')
# sleep(3)
# chrome.find_element(By.NAME, 'message').send_keys('Hello. Ce mai faceti?')
# sleep(3)
#
# chrome.quit()
#
#
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get('https://the-internet.herokuapp.com/')
# sleep(2)
#
# # selector by LINK_TEXT/PARTIAL_LINK_TEXT
# chrome.find_element(By.LINK_TEXT, 'Frames').click()
# sleep(3)
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Nested').click()
# sleep(3)
# chrome.quit()


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

chrome.get('https://jules.app/sign-in')

# selector by TAG
chrome.find_element(By.TAG_NAME, 'input').send_keys('roxana@crisan')
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input')
lista_taguri[1].send_keys('password')
print(len(lista_taguri))
sleep(3)
lista_taguri.clear()
sleep(3)
chrome.quit()