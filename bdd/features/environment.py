import time
from selenium import webdriver

def before_scenario(context,scenario):
    context.driver = webdriver.Chrome()

def after_scenario(context,scenario):
    context.driver.quit()

def after_step(context, step):
    time.sleep(1)

