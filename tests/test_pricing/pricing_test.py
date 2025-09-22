import allure
from selene import browser, have, query


@allure.tag("web", "pricing")
@allure.feature("Pricing")
@allure.link("https://www.pandadoc.com/pricing/", name="Pricing page")
class TestPricing:

    @allure.tag("smoke")
    @allure.story("Plans & CTA")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_pricing_plans_cta(self, setup_browser, pricing_page):

        pricing_page.open().start_free_trial()
        browser.element('h1').should(have.text('Start a free 14-day trial'))


    @allure.tag("regression")
    @allure.story("Plan price toggle")
    @allure.severity(allure.severity_level.NORMAL)
    def test_starter_pricing(self, setup_browser, pricing_page):
        annual_expected, monthly_expected = pricing_page.open().read_expected_starter_prises()

        pricing_page.starter_price.should(have.text(annual_expected))
        pricing_page.toggle_billing().click()
        pricing_page.starter_price.should(have.text(monthly_expected))