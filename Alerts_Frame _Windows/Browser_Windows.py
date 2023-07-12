import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        driver_path = r'C:\driver\chromedriver.exe'
        os.environ["PATH"] += os.pathsep + driver_path

        self.driver = webdriver.Chrome(options=options)
    
    def test_browser_windows(self):
        driver = self.driver
        driver.get('https://demoqa.com/browser-windows')

        current_handle = driver.current_window_handle
        new_tab = driver.find_element(By.XPATH, '//*[@id="tabButton"]')
        new_tab.click()

        wait = WebDriverWait(driver, 10)
        new_handle = wait.until(EC.new_window_is_opened(current_handle))
        driver.switch_to.window(new_handle)

        
        current_handle = driver.current_window_handle
        window_button = driver.find_element(By.ID, 'windowButton')
        window_button.click()
        time.sleep(2)

        windows = driver.window_handles

        for window in windows:
            if window != current_handle:
                driver.switch_to.window(window)

        driver.close()

if __name__ == "__main__":
    unittest.main()