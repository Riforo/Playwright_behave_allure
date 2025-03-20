from behave import fixture
from playwright.sync_api import sync_playwright
import allure

@fixture
def start_browser(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.browser = browser
    context.page = browser.new_page()

@fixture
def attach_screan_if_fallure(context, step):
    if step.status == "failed":
        page = getattr(context, "page", None)
        if page and context.browser.is_connected():
            # Ждём полной загрузки страницы
            page.wait_for_load_state("networkidle")
            # Делаем скриншот
            screenshot = page.screenshot()
            # Прикрепляем скриншот к Allure
            allure.attach(
                body=screenshot,
                name=f"screenshot_{step.name}",
                attachment_type=allure.attachment_type.PNG
            )
    
