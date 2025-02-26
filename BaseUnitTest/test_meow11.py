import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

class TestAbs(unittest.TestCase):

    def test_registration1(self):
        try:
            browser = webdriver.Chrome()
            browser.get("https://suninjuly.github.io/registration1.html")
            required_elements = browser.find_elements(By.CSS_SELECTOR, '[required]')
            a = 0
            for element in required_elements:
                match a:
                    case 0:
                        element.send_keys("Test")
                        a+= 1
                    case 1:
                        element.send_keys("Testovich")
                        a+= 1
                    case 2:
                        element.send_keys("Testom@gmail.com")
                        a+= 1
                    case _:
                        print('Errooor')
            buttonElement = browser.find_element(By.CLASS_NAME, "btn.btn-default")
            buttonElement.click()
            result = browser.find_element(By.TAG_NAME,"h1").text
            self.assertEqual(result,"Congratulations! You have successfully registered!","Тест 1 не дошёл до поздравлений(") 

        finally:
            browser.quit()
            
    def test_registration2(self):
        try:
            browser = webdriver.Chrome()
            browser.get("https://suninjuly.github.io/registration2.html")
            required_elements = browser.find_elements(By.CSS_SELECTOR, '[required]')
            a = 0
            for element in required_elements:
                match a:
                    case 0:
                        element.send_keys("Test")
                        a+= 1
                    case 1:
                        element.send_keys("Testom@gmail.com")
                        a+= 1
                    case _:
                        print('Errooor')
            buttonElement = browser.find_element(By.CLASS_NAME, "btn.btn-default")
            buttonElement.click()
            result = browser.find_element(By.TAG_NAME,"h1").text
            self.assertEqual(result,"Congratulations! You have successfully registered!","Тест 2 не дошёл до поздравлений(") 

        finally:
            browser.quit()
        
    
if __name__ == "__main__":
    unittest.main()
