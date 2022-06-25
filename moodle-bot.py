from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from getpass import getpass
from selenium.webdriver.firefox.options import Options as FirefoxOptions


browser = webdriver.Firefox(executable_path='/home/pajaro/Julián/Programación/moobot/geckodriver')


options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://moodle.psico.unlp.edu.ar/")

#busca caja de ingresar usuario y escribe 
username_box = driver.find_element_by_id("username")
username_box.send_keys("soporte")

#busca caja de ingresar contraseña y escribe 

pw_box = driver.find_element_by_id("password")
pw_box.send_keys("Grugru333")
# driver.implicitly_wait(0.5)
pw_box.send_keys(Keys.ENTER) #así se manda enter

### HASTA ARRIBA DE ESTO YA PONE USUARIO, CONTRASEÑA Y ENTRA.
### ABAJO NO ANDA.
open_menu_key = driver.find_element_by_class_name("yui_3_17_2_1_1645309176381_176")
open_menu_key.click()



