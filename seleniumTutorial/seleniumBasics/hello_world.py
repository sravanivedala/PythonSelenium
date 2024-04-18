'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)

'''2. Navigate to practice site'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3. Interact with the web elements'''
wiki_search_txtbx=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki_search_txtbx.send_keys("selenium")


wiki_search_btn=driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
wiki_search_btn.click()

name_txtbx=driver.find_element(By.XPATH,'//*[@id="name"]')
name_txtbx.send_keys("Sravani")


email_txtbx=driver.find_element(By.XPATH,'//*[@id="email"]')
email_txtbx.send_keys("Sravani@gmail.com")

phone_txtbx=driver.find_element(By.XPATH,'//*[@id="phone"]')
phone_txtbx.send_keys("8331919021")

male_gender=driver.find_element(By.ID,"male")
male_gender.click()
time.sleep(2)
female_gender=driver.find_element(By.ID,"female")
female_gender.click()
time.sleep(2)
male_gender.click()

day_sunday=driver.find_element(By.XPATH,'//*[@id="post-body-1307673142697428135"]/div[4]/div[1]')
day_sunday.click()
day_monday=driver.find_element(By.XPATH,'//*[@id="post-body-1307673142697428135"]/div[4]/div[2]/label')
day_monday.click()

country_1=driver.find_element(By.XPATH,'//*[@id="country"]/option[6]')
country_1.click()

time.sleep(2)
country_2=driver.find_element(By.XPATH,'//*[@id="country"]/option[5]')
country_2.click()
