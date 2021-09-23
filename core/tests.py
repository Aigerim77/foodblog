from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class SeleniumTest(TestCase):
    def test_one(self):
        driver = webdriver.Chrome()
        driver.get("http://www.localhost:8000/recipes/create")
        #driver.find_element_by_link_text("Советы").click()
        
        name = driver.find_element_by_name('name')
        name.send_keys('Тестовое название')

        short_description = driver.find_element_by_name('short_description')
        short_description.send_keys('Тестовое описание')
   
        description = driver.find_element_by_name('description')
        description.send_keys('Тестовая запись')
        
        button = driver.find_element_by_xpath("//*[contains(text(), 'Сохранить')]")
        button.click()

        sleep(5)
        drive.close()     