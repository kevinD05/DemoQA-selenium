from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_progress_bar_interaction(self):
        driver = self.driver
        driver.get('https://demoqa.com/progress-bar')

        start_button = driver.find_element(By.ID, 'startStopButton')
        start_button.click()
        time.sleep(5)  

        stop_button = driver.find_element(By.ID, 'startStopButton')
        stop_button.click()
        time.sleep(2)  

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report_progress_bar'))
