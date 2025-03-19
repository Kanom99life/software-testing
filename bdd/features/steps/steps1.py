from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from behave import *


@given(u'ฉันเข้าไปที่หน้าเว็บหลักของ Swag Lab')
def step_impl(context):
    context.driver.get('https://www.saucedemo.com/v1/index.html')


@then(u'ฉันจะเห็นว่าในหน้าเว็บมี title ที่เขียนว่า "{title}"')
def step_impl(context, title):
    web_title = context.driver.title
    assert web_title.lower() == title.lower()


@when(u'ฉันใส่ login ว่า "{username}"')
def step_impl(context,username):
    context.driver.find_element(By.ID, 'user-name').send_keys(username)


@when(u'ฉันใส่ password ว่า "{password}"')
def step_impl(context,password):
    context.driver.find_element(By.ID, 'password').send_keys(password)


@when(u'ฉันกดปุ่ม Login')
def step_impl(context):
    context.driver.find_element(By.ID, 'login-button').click()
    # context.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3').text

@then(u'ฉันต้องเห็นคำว่า "{product_label}" ขึ้นในหน้าเว็บ')
def step_impl(context, product_label):
    label = context.driver.find_element(By.CLASS_NAME, 'product_label').text
    assert label.lower() == product_label.lower()


@then(u'ระบบต้องแจ้งเตือนมาว่า "{errorMessage}"')
def step_impl(context, errorMessage):\
    assert errorMessage in context.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3').text


@when(u'ฉันกดปุ่ม ADD TO CART สักปุ่มบนหน้าจอ')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[3]/button').click()


@then(u'icon รูปบนตะกร้าต้องมีเลข 1 ขึ้นมา')
def step_impl(context):
    icon = context.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').text
    assert icon == '1'
    