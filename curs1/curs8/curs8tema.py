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


# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://jules.app/sign-in')
#
# # selector by TAG
# chrome.find_element(By.TAG_NAME, 'input').send_keys('roxana@crisan')
# lista_taguri = chrome.find_elements(By.TAG_NAME, 'input')
# lista_taguri[1].send_keys('password')
# print(len(lista_taguri))
# sleep(3)
# lista_taguri.clear()
# sleep(3)
# chrome.quit()


# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# chrome.find_element(By.XPATH, '/html/body/div/div/li[1]/a').click()
# sleep(3)
#
# # selector by Class
# lista_elemente_clasa = chrome.find_elements(By.CLASS_NAME, 'form-control')
# lista_elemente_clasa[0].send_keys('Home')
# lista_elemente_clasa[1].send_keys('Str Eliade')
# lista_elemente_clasa[2].send_keys('Str Mircea')
# lista_elemente_clasa[3].send_keys('Cluj')
# lista_elemente_clasa[4].send_keys('Cluj-Napoca')
# lista_elemente_clasa[6].send_keys('Romania')
# sleep(5)
# lista_elemente_clasa[2].clear
# sleep(3)
# chrome.quit()


# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# chrome.find_element(By.XPATH, '/html/body/div/div/li[1]/a').click()
# sleep(2)

# # selector by CSS - ID
# chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Home')  # # = identificator pentru id
# sleep(2)
# chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').clear()
# sleep(2)
# # selector by CSS - Class - only first one if multiple matches
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Acasa')  # . = identificator pentru clasa
# sleep(2)
# # selector by CSS - atribut=valoare
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Street address"]').send_keys('Str Eliade ')  # [] = identificator pentru atribut = valoare
# sleep(2)
# # selector by CSS - atribut=valoare partiala + parinte -> copil
# chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="Street address"]').send_keys('Mircea')  # * = marcator pentru valoare partiala a placeholderului
# sleep(3)
# chrome.quit()


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/autocomplete')

# selector by Xpath -> recomandat - cel mai flexibil
# selector by Xpath - atribut=valoare
chrome.find_element(By.XPATH, '//input[@id="autocomplete"]').send_keys('Acasa')
sleep(2)
# selector by Xpath - * toate elementele care resecta regula
chrome.find_element(By.XPATH, '//*[@id="street_number"]').send_keys('Str. Eliade')  #  * inseamna un inlocuitor pentru toate elementele care respecta regula
sleep(2)
# selector by Xpath - navigare in jos - trecem prin fiecare element
chrome.find_element(By.XPATH, '//div/div//input[@id="locality"]').send_keys('Cluj') # un div care are un copil div care are un input cu element id=locality
sleep(2)
# selector by Xpath - navigare in jos - skip tags - cautam oriunde sub form un input care sa respecte regula
chrome.find_element(By.XPATH, '//form//input[@id="administrative_area_level_1"]').send_keys('Cluj-Napoca') # // = orice mostenitor, / = primul mostenitor
sleep(2)
# selector by Xpath - selectare elem din lista - index incepe de la 1
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[6]').send_keys('Romania') # cerem sa scrie la al saselea element cu form control
sleep(3)

# selector by Xpath - OR primul gasit dintre variante
# | = SAU (ori prima conditie, ori a 2a, ori a 3a)
s = chrome.find_element(By.XPATH, '//input[@id="street_number"] | //input[@id="route"] | //input[@id="autocomplete"]') # oricare dintre elem gasite se stocheaza in acea variabila s
s.clear() # stergem valorile din input (primul identificat)
s.send_keys('Home') # punem altceva in acea variabila s dupa ce am sters (tot pe primul identificat)
sleep(3)

# # selector by Xpath - in care se foloseste parent ::
# chrome.find_element(By.XPATH, '//div[@class="form-control"]/parent::form').send_keys('ALABALA')
# sleep(3)

# # selector by Xpath - in care se foloseste frate
# chrome.find_element(By.XPATH, '//div[@class="form-control"]/parent::form/following-sibling::script').send_keys('MUAHAHAHA')
# sleep(3)

# o functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
def formy_input_by_placeholder(placeholder_text, input_value):
     input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
     input.clear()
     input.send_keys(input_value)

formy_input_by_placeholder('Zip code', '222555999000')
sleep(3)

# selector by Xpath - in f de textul vizibil
chrome.find_element(By.XPATH, '//a[text()="Formy"]').click() # aici cere sa fie exact acel text pe care sa se dea click
sleep(3)
chrome.quit()
