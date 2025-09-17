import allure
from selene import browser, be, have


@allure.feature("Forms")
@allure.story("Contact Sales")
@allure.severity(allure.severity_level.CRITICAL)
def test_submit_empty_contact_sales_form(setup_browser):
    with allure.step("Open Contact Sales page"):
        browser.open("/contact-sales/")
        if browser.element('.onetrust-close-btn-handler').matching(be.visible):
            browser.element('.onetrust-close-btn-handler').click()

    with allure.step("Click Schedule demo without filling fields"):
        browser.element('[data-testid="pd-button-submit-form"]').click()

    with allure.step("Verify validation errors are displayed"):
        browser.element('.hs-form-field.hs_company .hs-error-msg').should(have.exact_text('Please enter your company name'))