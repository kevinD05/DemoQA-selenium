
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

    def test_upload_download(self):
        driver = self.driver
        driver.get('https://demoqa.com/upload-download')

        # Haz clic en el botón "Upload File"
        upload_button = driver.find_element(By.ID, 'uploadFile')
        upload_button.click()
        time.sleep(2)

        # Haz clic en el botón "Download"
        download_button = driver.find_element(By.ID, 'downloadButton')
        download_button.click()

        time.sleep(3)

        # Realiza cualquier acción adicional después de subir y descargar el archivo

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'resultado de test upload and download'))