import allure
from selene import be, have
from panda_doc.pages.contact_sales_page import ContactSalesPage


@allure.tag("web", "regression", "forms")
@allure.feature("Forms")
@allure.story("Contact Sales form validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://www.pandadoc.com/contact-sales/", name="Contact Sales page")
def test_submit_empty_contact_sales_form(setup_browser, contact_sales):

    with allure.step("Open Contact Sales page"):
        contact_sales.open()
        contact_sales.close_cookies_if_visible()

    with allure.step("Click Schedule demo without filling fields"):
        contact_sales.submit_button.click()

    with allure.step("Verify validation errors are displayed"):
        contact_sales.company_error.should(have.exact_text('Please enter your company name'))