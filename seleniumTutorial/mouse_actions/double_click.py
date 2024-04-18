'''
Created on 11-Apr-2024

@author: Rakesh
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)

'''2. Navigate to practice site'''
driver.get("https://testautomationpractice.blogspot.com/")
copy_txt_btn=driver.find_element(By.CSS_SELECTOR,"#HTML10 > div.widget-content > button")
my_actions=ActionChains(driver)
my_actions.double_click(copy_txt_btn)
my_actions.perform()


