from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from behave import *

@given(u'ฉันเข้าไปที่หน้าเว็บ form ของ selenium')
def step_impl(context):
    context.driver.get('https://www.selenium.dev/selenium/web/web-form.html')


@then(u'ฉันจะเห็นว่าในหน้าเว็บมี heading ที่เขียนว่า Web form')
def step_impl(context):
    heading = context.driver.find_element(By.CSS_SELECTOR, 'h1')
    assert heading.text == 'Web form'

@then(u'ฉันใส่คำว่า "{textInput}" ลงใน text input')
def step_impl(context, textInput):
    context.driver.find_element(By.ID, 'my-text-id').send_keys(textInput)


@then(u'ฉันกดปุ่มที่เขียนว่า Default checkbox')
def step_impl(context):
    context.driver.find_element(By.ID, 'my-check-2').click()

@then(u'ฉันกดปุ่ม Submit')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    

@then(u'ฉันควรจะเห็น message ขึ้นว่า "{message}"')
def step_impl(context, message):
    assert context.driver.find_element(By.ID, 'message').text == message