import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        driver_path = r'C:\driver\chromedriver.exe'
        os.environ["PATH"] += os.pathsep + driver_path

        self.driver = webdriver.Chrome(options=options)

    def test_links(self):
        driver = self.driver
        driver.get('https://demoqa.com/links')

        # Obtén el identificador de la ventana activa actual
        current_window = driver.current_window_handle

        # Haz clic en el primer enlace
        simple_link = driver.find_element(By.ID, 'simpleLink')
        simple_link.click()
        time.sleep(2)

        # Espera hasta que se abra una nueva ventana o pestaña
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Obtén los identificadores de todas las ventanas abiertas
        windows = driver.window_handles

        # Cierra la nueva ventana o pestaña
        for window in windows:
            if window != current_window:
                driver.switch_to.window(window)
                driver.close()

        # Vuelve a la pestaña original
        driver.switch_to.window(current_window)

        # Realiza cualquier acción adicional en la pestaña original
        time.sleep(2)

        # Haz clic en el segundo enlace
        dynamic_link = driver.find_element(By.ID, 'dynamicLink')
        dynamic_link.click()
        time.sleep(2)

        # Espera hasta que se abra otra nueva ventana o pestaña
        WebDriverWait(driver, 20).until(lambda driver: len(driver.window_handles) > 1)


        # Obtén los identificadores de todas las ventanas abiertas
        windows = driver.window_handles

        # Cierra la nueva ventana o pestaña
        for window in windows:
            if window != current_window:
                driver.switch_to.window(window)
                driver.close()

        # Vuelve a la pestaña original
        driver.switch_to.window(current_window)

        # Realiza cualquier acción adicional en la pestaña original
        time.sleep(2)

        created = driver.find_element(By.ID, 'created')
        created.click()
        time.sleep(2)

        content = driver.find_element(By.ID, 'no-content')
        content.click()
        time.sleep(2)

        moved = driver.find_element(By.ID, 'moved')
        moved.click()
        time.sleep(2)

        request = driver.find_element(By.ID, 'bad-request')
        request.click()
        time.sleep(2)

        unauthorized = driver.find_element(By.ID, 'unauthorized')
        unauthorized.click()
        time.sleep(2)

        forbidden = driver.find_element(By.ID, 'forbidden')
        forbidden.click()
        time.sleep(2)

        not_found = driver.find_element(By.ID, 'invalid-url')
        not_found.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test de test link'))
 