from behave import use_fixture

from fixtures import *

def before_scenario(context, scenario):
    use_fixture(start_browser, context)

def after_step(context, step):
    use_fixture(attach_screan_if_fallure, context, step)

def after_all(context):
    if hasattr(context, "browser"):
        context.browser.close()
