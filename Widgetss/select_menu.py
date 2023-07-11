from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import unittest
import time

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_select_menu(self):
        driver = self.driver
        driver.get('https://demoqa.com/select-menu')
        time.sleep(3)

        select = driver.find_element(By.XPATH, '//div[@class="css-1hwfws3"]')
        select.click()
        time.sleep(2)

        select_title = driver.find_element(By.XPATH, '//div[@class=" css-1wa3eu0-placeholder"]')
        select_title.click()

        # Esperar a que las opciones estén visibles

        opciones = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class=" css-1uccc91-singleValue"]'))   
            )

        # Seleccionar una opción
        opcion = driver.find_element(By.XPATH, '//div[@class=" css-1uccc91-singleValue"][text()="Group 1, option 2"]')
        opcion.click()

        select3 = driver.find_element(By.XPATH, '//*[@id="oldSelectMenu"]')
        opcions = select3.find_elements(By.TAG_NAME, 'option')
        time.sleep(3)
        for option in opcions:
            print('Los valores son: %s' % option.get_attribute('value'))
            option.click()
            time.sleep(2)
            seleccionar = Select(driver.find_element(By.XPATH, '//div[@class=" css-1uccc91-singleValue"][text()="Group 1, option 2"]'))
            seleccionar.select_by_value('10')
            time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()