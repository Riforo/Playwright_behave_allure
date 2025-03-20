from playwright.async_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    __URL_PAGE = "https://test.ru/"
    __LOGIN_FILD = "Логин"
    __PASSWORD_FILD = "Пароль"
    __BUTTON_LOGIN = "Войти"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.get_by_placeholder(self.__LOGIN_FILD)
        self.password = page.get_by_placeholder(self.__PASSWORD_FILD)
        self.login_button = page.get_by_role('button', name=self.__BUTTON_LOGIN)

    def navigate(self):
        self.page.goto(self.__URL_PAGE)
        self.page.wait_for_load_state("domcontentloaded")

    def fill_username(self, text):
        self.username.fill(text)

    def fill_password(self, text):
        self.password.fill(text)

    def clic_login_button(self):
        self.login_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        

    def fill_form_field(self, field, value):
        if field == "логин":
            self.fill_username(value)
        elif field == "пароль":
            self.fill_password(value)
        else:
            assert False
    
    def clic_button(self, button):
        if button == "Войти":
            self.clic_login_button()
