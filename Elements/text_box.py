import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import HtmlTestRunner

class UsandoUnittest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        driver_path = r'C:\driver\chromedriver.exe'
        os.environ["PATH"] += os.pathsep + driver_path
     
        self.driver = webdriver.Chrome(options=options)
    
    def test_rellenar_textbox(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")

       # Encontrar el elemento por su atributo id
        campo1 = driver.find_element(By.ID, 'userName')
        campo1.send_keys('alexander diaz')
        time.sleep(1)

        campo2 = driver.find_element(By.ID, 'userEmail')
        campo2.send_keys('alexanderkevindiaz05@gmail.com')
        time.sleep(1)

        campo3 = driver.find_element(By.ID, 'currentAddress')
        campo3.send_keys('123345')
        time.sleep(1)

        campo3 = driver.find_element(By.ID, 'permanentAddress')
        campo3.send_keys('123345')
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        # Encontrar el botón por su atributo class y hacer clic en él
        boton_submit = driver.find_element(By.ID, 'submit')
        boton_submit.click()
        time.sleep(2)
 
        
if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'resultado de test text box'))