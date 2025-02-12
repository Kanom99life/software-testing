from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)
title = driver.title
assert title == "Web form"

try:
	heading = driver.find_element(By.CSS_SELECTOR,'h1')
	assert heading.text == "Web form"
except NoSuchElementException:
	assert False,"The element doesn't exist"

#----something more under here ------







#------------------------------------

#end the code with
driver.quit()