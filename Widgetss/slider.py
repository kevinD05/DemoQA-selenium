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

    def test_slider_interaction(self):
        driver = self.driver
        driver.get('https://demoqa.com/slider')

        slider = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/form/div/div[1]/span/input')
        time.sleep(2)

        slider_width = slider.size['width']
        slider_height = slider.size['height']

        actions = ActionChains(driver)
        actions.click_and_hold(slider).move_by_offset(slider_width/2, 0).release().perform()

        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report_test slider'))
