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

    def test_radio_button(self):
        driver = self.driver
        driver.get("https://demoqa.com/radio-button")

        yes = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]')
        yes.click()
        time.sleep(2)

        impressive = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]')
        impressive.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test radio button '))