import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from dotenv import load_dotenv
import os
from selene import browser
from utils import attach
from panda_doc.pages.pricing_page import PricingPage
from panda_doc.pages.home_page import HomePage
from panda_doc.pages.templates_page import TemplatesPage
from panda_doc.pages.request_demo_page import RequestDemoPage
from panda_doc.pages.contact_sales_page import ContactSalesPage

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def remote_browser_setup(request):

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
    yield browser
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    try:
        browser.quit()
    except (InvalidSessionIdException, WebDriverException):
        pass

@pytest.fixture()
def pricing_page():
    return PricingPage()

@pytest.fixture()
def home_page():
    return HomePage()

@pytest.fixture()
def contact_sales():
    return ContactSalesPage()

@pytest.fixture()
def request_demo():
    return RequestDemoPage()

@pytest.fixture()
def templates_page():
    return TemplatesPage()

@pytest.fixture(autouse=True)
def setup_browser(remote_browser_setup):
    base_url = os.getenv("BASE_URL")
    browser.config.base_url = base_url
    browser.config.timeout = 5
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield