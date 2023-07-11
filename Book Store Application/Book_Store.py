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

    def test_book_store(self):
        driver = self.driver
        driver.get('https://demoqa.com/books')

        buscar = driver.find_element(By.XPATH, '//*[@id="searchBox"]')
        buscar.click()
        buscar.send_keys('designing')
        time.sleep(2)

        libro = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/span/a')
        libro.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        agregar = driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]')
        agregar.click()
        alerta = driver.switch_to.alert
        alerta.accept()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test de book store'))