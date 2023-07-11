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

    def test_login(self):
        driver = self.driver
        driver.get('https://demoqa.com/login')

        user = driver.find_element(By.XPATH, '//*[@id="userName"]')
        user.send_keys('chester')
        time.sleep(2)

        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('~$3q~-X2uXrAvd.')
        time.sleep(2)

        boton = driver.find_element(By.XPATH, '//*[@id="login"]')
        boton.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report_login'))