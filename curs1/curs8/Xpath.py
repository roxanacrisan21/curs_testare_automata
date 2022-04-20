# XPATH
# adresa de la inceputul pana unde se gaseste elementul nostru (la inspection se da click dreapta + copy xpath/full xpath)
# in browser numaratoarea incepe de la 1 si continua
# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
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

# Xpath -> recomandat - cel mai flexibil

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Xpath - atribut=valoare
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('A')

sleep(2)

# selector by Xpath - * toate elementele care resecta regula
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('n')  #  * inseamna un inlocuitor pentru toate elementele care respecta regula

sleep(2)

# selector by Xpath - navigare in jos - trecem prin fiecare element
chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('r') # un div care are un copil div care are un input cu element id=first-name

sleep(2)

# selector by Xpath - navigare in jos - skip tags - cautam oriunde sub form un input care sa respecte regula
chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('e') # // = orice mostenitor, / = primul mostenitor
sleep(2)

# selector by Xpath - selectare elem din lista - index incepe de la 1
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('i') # cerem sa scrie la al doilea element cu form control

sleep(3)


# selector by Xpath - OR primul gasit dintre variante
# | = SAU (ori prima conditie, ori a 2a, ori a 3a)
s = chrome.find_element(By.XPATH, '//input[@id="last-name1"] | //input[@id="last-name2"] | //input[@id="last-name"]') # oricare dintre elem gasite se stocheaza in acea variabila s

s.clear() # stergem valorile din input (primul identificat)
s.send_keys('Sinpetrean') # punem altceva in acea variabila s dupa ce am sters (tot pe primul identificat)

# selector by Xpath - in f de textul partial + luam textul de pe el cu proprietatea text
full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').text # extrage textul din interiorul unui element
print(full_text) # printeaza pe ecram textul gasit si incepe cu "Sub"
assert full_text == 'Submit' # se verifica daca textul intreg gasit (extras) este egal cu ce am scris "Submit" (ce il asteptam)

label_result = chrome.find_element(By.XPATH, '//label[@for="first-name"]').text
print(label_result)
assert label_result == 'First name'

sleep(3)

# selector by Xpath - in f de textul vizibil
chrome.find_element(By.XPATH, '//a[text()="Submit"]').click() # aici cere sa fie exact acel text pe care sa se dea click

''' cautam si pe site la inspection, scriem in partea de jos
x y axis navigation
cu parent in sus
cu / elem_type - ajungem la elementul copil
cu // elem_type - cauta prin toti descendentii
cu parent::elem_type in sus
cu following-sibling::elem_type - urmatorul frate de la acelasi nivel
cu preceding-sibling::elem_type - fratele anterior de la acelasi nivel
//label[text()="First name"]/parent::strong/following-sibling::input/preceding-sibling::strong
'''
# exemplu cautare pentru copil:
# /div[@class=“form-group”]/div/strong/label[@for=“first-name”]
# //div[@class=“form-group”]/div[2]


# cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip
# si vrem sa parametrizam selectorul
def formy_input_by_placeholder(placeholder_text, input_value):
    input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input.clear()
    input.send_keys(input_value)


def formy_input_by_label(label, input_value):
    my_input = chrome.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
    my_input.clear()
    my_input.send_keys(input_value)


formy_input_by_placeholder('Enter first name', 'ANDY')
formy_input_by_placeholder('Enter last name', 'SINPETREAN')

formy_input_by_label('Job title', 'Automation Engineer')

sleep(3)
chrome.quit()