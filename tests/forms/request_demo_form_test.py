import allure
from selene import browser, be, have


@allure.feature("Forms")
@allure.story("Request a Demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_submit_empty_request(setup_browser):
    with allure.step("Open Request a Demo form"):
        browser.open("/getdemo/")

    with allure.step("Click Submit with all required fields empty"):
        browser.element('[data-testid="pd-button-submit-form"]').click()

    with allure.step("Verify validation errors are displayed"):
        browser.element('.hs-form-field.hs_email .hs-error-msg').should(have.text('Please enter a valid email address'))


@allure.feature("Forms")
@allure.story("Request a Demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_email_without_phone(setup_browser):
    with allure.step("Open Request a Demo form"):
        browser.open("/getdemo/")

    with allure.step("Fill valid email and submit"):
        browser.element('[name="email"]').type("abc@ads.abs")
        browser.element('[data-testid="pd-button-submit-form"]').click()

    with allure.step("Verify phone validation error is shown"):
        browser.element(".hs-form-field.hs_phone .hs-error-msg").should(have.text("Please enter a valid phone number"))