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

    def test_modal_dialogs(self):
        driver = self.driver
        driver.get('https://demoqa.com/modal-dialogs')

        small = driver.find_element(By.XPATH, '//*[@id="showSmallModal"]')
        small.click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        windows = driver.window_handles
        driver.switch_to.window(windows[1])

        close_button = driver.find_element(By.XPATH,'//*[@id="closeSmallModal"]')
        close_button.click()
        driver.switch_to.window(windows[0])

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()