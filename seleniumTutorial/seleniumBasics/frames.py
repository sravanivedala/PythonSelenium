'''
Created on 09-Apr-2024

@author: Rakesh
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("Start-maximized")
driver=webdriver.Chrome(my_options)

'''2. Navigate to practice site'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3. Switch to the frame'''
driver.switch_to.frame("frame-one796456169")

'''4. Enter your name in Name field under Frames'''
name_txt_bx=driver.find_element(By.ID,"RESULT_TextField-0")
name_txt_bx.send_keys("Sravani")

gender_male=driver.find_element(By.CSS_SELECTOR,"#q2 > table > tbody > tr:nth-child(1) > td > label")
gender_male.click()

time.sleep(5)
gender_female=driver.find_element(By.CSS_SELECTOR,"#q2 > table > tbody > tr:nth-child(2) > td > label")
gender_female.click()

'''5. Exit from the frame'''
driver.switch_to.parent_frame() # exiting the frame