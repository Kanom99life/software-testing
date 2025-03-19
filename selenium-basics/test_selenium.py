import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# pytest --cache-clear -v

@pytest.fixture
def driver():
	driver = webdriver.Chrome()
	#driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get("https://www.lambdatest.com/selenium-playground")
	driver.implicitly_wait(5)
	yield driver
	driver.quit()


def test_one(driver):
	send_text = "Selenium Automation"
	driver.find_element(By.XPATH, "//a[@href='https://www.lambdatest.com/selenium-playground/simple-form-demo']").click()
	driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys(send_text)
	driver.find_element(By.XPATH, "//button[@id='showInput']").click()
	assert driver.find_element(By.XPATH, "//p[@id='message']").text == send_text


def test_two(driver):
	driver.find_element(By.XPATH, "//a[@href='https://www.lambdatest.com/selenium-playground/checkbox-demo']").click()
	checkboxes = [
        (By.ID, "ex1-check1"),
        (By.ID, "ex1-check2"),
        (By.XPATH, "(//input[@id='ex1-check3'])[1]"),
        (By.XPATH, "(//input[@id='ex1-check3'])[2]")
    ]
	for locator in checkboxes:
		assert driver.find_element(*locator).is_selected() == False
	driver.find_element(By.XPATH, "//input[@id='box']").click()
	for locator in checkboxes:
		assert driver.find_element(*locator).is_selected()


def test_three(driver):
	driver.find_element(By.XPATH, "//a[@href='https://www.lambdatest.com/selenium-playground/select-dropdown-demo']").click()
	driver.find_element(By.XPATH, "//select[@id='select-demo']/option[text()='Friday']").click()
	selected_value = driver.find_element(By.XPATH, "//select[@id='select-demo']/option[text()='Friday']").text
	assert driver.find_element(By.CLASS_NAME, "selected-value").text == f"Day selected :- {selected_value}"


def test_four(driver):
	driver.find_element(By.XPATH, "//a[@href='https://www.lambdatest.com/selenium-playground/bootstrap-download-progress-demo']").click()
	assert driver.find_element(By.CLASS_NAME, "counter").text == "0%"
	driver.find_element(By.XPATH, "//button[@id='dwnBtn']").click()
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "success")) ) 
	assert driver.find_element(By.CLASS_NAME, "counter").text == "100%"
	assert driver.find_element(By.CLASS_NAME, "success").text == "Download completed!"


def test_five(driver):
	driver.find_element(By.XPATH, "//a[@href='https://www.lambdatest.com/selenium-playground/download-file-demo']").click()
	driver.find_element(By.XPATH, "//button[@type='button' and @class='btn btn-primary']").click()
	file_path = os.path.expanduser('~/Downloads/LambdaTest.pdf')
	while not os.path.exists(file_path):
		time.sleep(1)
	assert os.path.exists(file_path)
	if os.path.exists(file_path):
		os.remove(file_path)
	assert not os.path.exists(file_path)