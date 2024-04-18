'''
Created on 18-Apr-2024

@author: Rakesh
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)

'''2. Navigate to practice site'''
driver.get("https://testautomationpractice.blogspot.com/")

country_drop_down=driver.find_element(By.ID, "country")

'''3. Selecting options from drop-down menu'''

my_select=Select(country_drop_down)
my_select.select_by_index(2)
time.sleep(5)
my_select.select_by_value('australia')
time.sleep(5)
my_select.select_by_visible_text("India")
