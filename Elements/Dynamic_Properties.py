
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

    def test_upload_download(self):
      driver = self.driver
      driver.get('https://demoqa.com/dynamic-properties')
      

      color = driver.find_element(By.XPATH, '//*[@id="colorChange"]')
      color.click()
      time.sleep(5)

      after = driver.find_element(By.XPATH, '//*[@id="visibleAfter"]')
      after.click(3)

      enable = driver.find_element(By.XPATH,'//*[@id="enableAfter"]')
      enable.click()
      time.sleep(2)

    def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test dynamic properties '))
      