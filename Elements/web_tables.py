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

    def test_web_table(self):
        driver = self.driver
        driver.get("https://demoqa.com/webtables")

        # Editar usuario
        editar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'edit-record-1')))
        editar.click()
        time.sleep(2)

        # Cerrar ventana
        cerrar = driver.find_element(By.CSS_SELECTOR, 'button.close')
        cerrar.click()
        
        # Buscar por nombre
        add = driver.find_element(By.ID, 'searchBox')
        add.send_keys('alden')
        time.sleep(2)

        # Esperar a que aparezca el botón de eliminación
        delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id^="delete-record-"]')))
        delete.click()
        time.sleep(2)

        # Hacer clic en el botón "Add"
        add_button = driver.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        time.sleep(2)

        # Agregar información a las casillas vacías
        first_name = driver.find_element(By.ID, 'firstName')
        last_name = driver.find_element(By.ID, 'lastName')
        email = driver.find_element(By.ID, 'userEmail')
        age = driver.find_element(By.ID, 'age')
        salary = driver.find_element(By.ID, 'salary')
        department = driver.find_element(By.ID, 'department')

        if first_name.get_attribute('value') == '':
            first_name.send_keys('Nombre')

        if last_name.get_attribute('value') == '':
            last_name.send_keys('Apellido')

        if email.get_attribute('value') == '':
            email.send_keys('name@example.com')

        if age.get_attribute('value') == '':
            age.send_keys('25')

        if salary.get_attribute('value') == '':
            salary.send_keys('5000')

        if department.get_attribute('value') == '':
            department.send_keys('Departamento')

        # Hacer clic en el botón "Submit"
        submit_button = driver.find_element(By.ID, 'submit')
        submit_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'report test web tables'))
