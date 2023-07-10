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

    def test_alerts(self):
        driver = self.driver
        driver.get('https://demoqa.com/alerts')

        button1 = driver.find_element(By.ID, 'alertButton')
        button1.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        time.sleep(3)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)

        button2 = driver.find_element(By.ID, 'timerAlertButton')
        button2.click()
        time.sleep(6)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        alert2.accept()
        time.sleep(3)

        button3 = driver.find_element(By.ID, 'confirmButton')
        button3.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert3 = driver.switch_to.alert
        alert3.accept()
        time.sleep(3)

        button4 = driver.find_element(By.ID, 'promtButton')
        button4.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert4 = driver.switch_to.alert
        alert4.send_keys('kevin')
        alert4.accept()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test de test alerts'))
 
