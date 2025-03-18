from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
import allure

@fixture
def browser_chrome(context):
    p = sync_playwright().start
    browser = p.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
    context.browser = browser
    context.page = browser.new_page()
    return context.page

def before_scenario(context, scenario):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.browser = browser
    context.page = browser.new_page()

def after_step(context, step):
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

def after_all(context):
    if hasattr(context, "browser"):
        context.browser.close()
