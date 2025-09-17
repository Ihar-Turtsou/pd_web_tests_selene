import allure
from selene import be, have
from src.pages.contact_sales_page import ContactSalesPage


@allure.tag("web", "regression", "forms")
@allure.feature("Forms")
@allure.story("Contact Sales form validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://www.pandadoc.com/contact-sales/", name="Contact Sales page")
def test_submit_empty_contact_sales_form(setup_browser):
    sales_page = ContactSalesPage()

    with allure.step("Open Contact Sales page"):
        sales_page.open_sales()
        sales_page.close_cookies_if_visible()

    with allure.step("Click Schedule demo without filling fields"):
        sales_page.submit_button.click()

    with allure.step("Verify validation errors are displayed"):
        sales_page.company_error.should(have.exact_text('Please enter your company name'))