import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
    
    def test_buttons(self):
        driver = self.driver
        driver.get('https://demoqa.com/buttons')

        double_clic = driver.find_element(By.ID, 'doubleClickBtn')
        actions = ActionChains(driver)
        actions.double_click(double_clic).perform()
        time.sleep(5)

        clic_derecho = driver.find_element(By.ID, 'rightClickBtn')
        derecho = ActionChains(driver)
        derecho.context_click(clic_derecho).perform()
        time.sleep(5)

        clic_me = driver.find_element(By.XPATH, '//button[contains(text(), "Click Me")]')
        clic_me.click()
        time.sleep(3)  
         
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # Guardar el resultado de la prueba en un archivo HTML
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'resultado de test buttons'))
