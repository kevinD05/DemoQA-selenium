import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
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

    def test_automatizacion(self):
        driver = self.driver
        driver.get("https://demoqa.com/checkbox")

        # Hacer clic en el primer botón
        boton_toggle = driver.find_element(By.CLASS_NAME, 'rct-collapse-btn')
        boton_toggle.click()
        time.sleep(2)
        
        # Hacer clic en el segundo botón
        expand_icon = driver.find_element(By.CSS_SELECTOR, 'svg.rct-icon-expand-all')
        expand_icon.click()
        time.sleep(2)

        # Hacer clic en el checkbox
        checkbox = driver.find_element(By.CSS_SELECTOR, 'span.rct-checkbox')
        checkbox.click()
        time.sleep(2)

        # Regresar a la página anterior
        driver.back()

        # Cerrar el navegador
        driver.quit()


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'test check box report'))