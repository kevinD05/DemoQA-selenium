import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        driver_path = r'C:\driver\chromedriver.exe'
        os.environ["PATH"] += os.pathsep + driver_path

        self.driver = webdriver.Chrome(options=options)
        
    def test_practice_form(self):
        driver = self.driver
        driver.get('https://demoqa.com/automation-practice-form')

        name = driver.find_element(By.ID, 'firstName')
        name.send_keys('Kevin')
        time.sleep(2)

        apellido = driver.find_element(By.ID, 'lastName')
        apellido.send_keys('Diaz')
        time.sleep(2)

        email = driver.find_element(By.ID, 'userEmail')
        email.send_keys('alexanderkevindiaz05@gmail.com')
        time.sleep(2)

        genero = driver.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label')
        genero.click()
        time.sleep(2)

        numero = driver.find_element(By.XPATH, '//*[@id="userNumber"]')
        numero.send_keys('57369399')
        time.sleep(2)

        hobbie = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[1]/label')
        hobbie.click()
        time.sleep(2)

        dress = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
        dress.send_keys('de la terminal de la 119, 2 al sur, 2 arriba')
        time.sleep(2)


        submit = driver.find_element(By.XPATH, '//*[@id="submit"]')
        submit.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test practice form'))
