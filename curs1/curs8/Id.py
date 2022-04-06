# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # descarcare chrome
from selenium.webdriver.common.by import By # pt accesarea elementelor din interfata

# initializam chrome
s = Service(ChromeDriverManager().install()) # stocam serviciul de Chrome
chrome = webdriver.Chrome(service=s) # definim o noua variabila in care stocam acel serviciu, adica driverul de chrome

# maximizam fereastra
chrome.maximize_window() # metoda folosita pentru maximizarea fereastra browserului

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form') # metoda get este o metoda prin care putem naviga la un anumit link

# selector by ID
# numele il gasim in pagina web daca dam click drepta pe acel tab si dam inspect - de acolo se ia numele id-ului
first_name = chrome.find_element(By.ID, 'first-name') # metoda find element este o metoda prin care putem sa cautam u  element in codul de html pe baza de diversi identificatori
first_name.send_keys('Ala Bala Portocala') # metoda send_keys este o metoda care scrie ceva intr-un camp din browser

sleep(3) # folosim metoda sleep sa putem instrui sistemul sa astepte putin inainte sa mearga mai departe

chrome.quit() # o metoda care este folosita pentru a inchide browserul