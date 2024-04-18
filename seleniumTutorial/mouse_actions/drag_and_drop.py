'''
Created on 11-Apr-2024

@author: Rakesh
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#import time
'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)

'''2. Navigate to practice site'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3.a.Drag and drop by source and target '''
source=driver.find_element(By.ID, "draggable")
target=driver.find_element(By.ID, "droppable")
my_actions=ActionChains(driver)
#my_actions.scroll_to_element(target)
my_actions.scroll_by_amount(0,500).perform()


my_actions.drag_and_drop(source, target).perform()
#my_actions.perform()

'''3.b. Drag and drop by offset '''
#my_actions.drag_and_drop_by_offset(source, 100, 0).perform()

slider=driver.find_element(By.CSS_SELECTOR, "#slider > span")
my_actions.click_and_hold(slider).perform()
my_actions.move_by_offset(150, 0).perform()
#my_actions.move_to_element_with_offset(slider, 150, 0).perform()

my_actions.release(slider).perform()

resizable=driver.find_element(By.CSS_SELECTOR, "#resizable > div.ui-resizable-handle.ui-resizable-se.ui-icon.ui-icon-gripsmall-diagonal-se")
my_actions.click_and_hold(resizable).perform()
my_actions.move_by_offset(100,0).perform()
#my_actions.move_to_element_with_offset(resizable, -200, 0).perform()
my_actions.release(resizable).perform()
