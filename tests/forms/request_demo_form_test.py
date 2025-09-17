import allure
from selene import have
from src.pages.request_demo_page import RequestDemoPage


@allure.tag("web", "regression", "forms")
@allure.feature("Forms")
@allure.story("Request a Demo form validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://www.pandadoc.com/getdemo/", name="Request a Demo page")
def test_submit_empty_request(setup_browser):
    request_demo = RequestDemoPage()

    with allure.step("Open Request a Demo form"):
        request_demo.open()

    with allure.step("Click Submit with all required fields empty"):
        request_demo.submit_button.click()

    with allure.step("Verify validation error for email is displayed"):
        request_demo.email_error.should(have.exact_text("Please enter a valid email address"))


@allure.tag("web", "regression", "forms")
@allure.feature("Forms")
@allure.story("Request a Demo form validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://www.pandadoc.com/getdemo/", name="Request a Demo page")
def test_valid_email_without_phone(setup_browser):
    request_demo = RequestDemoPage()

    with allure.step("Open Request a Demo form"):
        request_demo.open()

    with allure.step("Fill email and submit without phone"):
        request_demo.email_input.type("abc@ads.abs")
        request_demo.submit_button.click()

    with allure.step("Verify phone validation error is displayed"):
        request_demo.phone_error.should(have.exact_text("Please enter a valid phone number"))