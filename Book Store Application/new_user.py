from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
import HtmlTestRunner

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_new_user(self):
        driver = self.driver
        driver.get('https://demoqa.com/login')

        new_user = driver.find_element(By.XPATH, '//*[@id="newUser"]')
        new_user.click()
        time.sleep(1)

        name = driver.find_element(By.XPATH, '//*[@id="firstname"]')
        name.send_keys('kevin')
        time.sleep(2)

        apellido = driver.find_element(By.XPATH, '//*[@id="lastname"]')
        apellido.send_keys('diaz')
        time.sleep(2)

        user_name = driver.find_element(By.XPATH, '//*[@id="userName"]')
        user_name.send_keys('mike')
        time.sleep(2)

        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('~$3q~-X2uXrAvd.')
        time.sleep(1)

        boton = driver.find_element(By.XPATH, '//*[@id="register"]')
        boton.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()