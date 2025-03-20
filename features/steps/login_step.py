from behave import *

from pages.login_page import LoginPage
    

@given("Я нахожусь на странице авторизации")
def open_login_url(context):
    login_page = LoginPage(context.page)
    login_page.navigate()

@when("Я ввожу в поле {fild} значение {value} на странице авторизации")
def set_login(context, fild: str, value: str):
    login_page = LoginPage(context.page)
    login_page.fill_form_field(fild, value)

@when("Я нажимаю кнопку {button} на странице авторизации")
def clic_button(context, button: str):
    login_page = LoginPage(context.page)
    login_page.clic_button(button)

@then("Я авторизовался и жту таймаута")
def page_wait(context):
    login_page = LoginPage(context.page)
    login_page.page.wait_for_timeout(10000)

@then("Сравниваю чсило {one} и числом {twoo}")
def check_nember(context, one, twoo):
    assert one == twoo
