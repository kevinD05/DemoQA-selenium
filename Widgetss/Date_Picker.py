import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import HtmlTestRunner

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_data_picker(self):
        driver = self.driver
        driver.get('https://demoqa.com/date-picker')

        dia = driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')
        dia.click()

        dia_ = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[4]')
        dia_.click()
        time.sleep(2)

        hora_dia = driver.find_element(By.XPATH, '//*[@id="dateAndTimePickerInput"]')
        hora_dia.click()
        time.sleep(1)

        hora_dia1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[4]')
        hora_dia1.click()
        time.sleep(2)

        horaa = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/ul/li[87]')
        horaa.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test data picker'))

    
