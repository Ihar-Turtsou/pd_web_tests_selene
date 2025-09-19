import allure
from selene import browser, have, query
from panda_doc.pages.pricing_page import PricingPage


@allure.tag("web", "pricing")
@allure.feature("Pricing")
@allure.link("https://www.pandadoc.com/pricing/", name="Pricing page")
class TestPricing:

    @allure.tag("smoke")
    @allure.story("Plans & CTA")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_pricing_plans_cta(self, setup_browser):
        pricing_page = PricingPage()

        with allure.step('Open the pricing page'):
            pricing_page.pricing_page_open()

        with allure.step("Verify Starter plan CTA leads to trial"):
            pricing_page.button_start_free_trial.click()

            browser.element('h1').should(have.text('Start a free 14-day trial'))


    @allure.tag("regression")
    @allure.story("Plan price toggle")
    @allure.severity(allure.severity_level.NORMAL)
    def test_starter_pricing(self, setup_browser):
        pricing_page = PricingPage()

        with allure.step('Open the pricing page'):
            pricing_page.pricing_page_open()

        with allure.step("Get expected values from attributes"):
           started_annual_expected = pricing_page.starter_price.get(query.attribute('data-toggleable-original'))
           started_monthly_expected = pricing_page.starter_price.get(query.attribute('data-toggleable-alternative'))

        with allure.step("Verify annual price is shown by default"):
            pricing_page.starter_price.should(have.text(started_annual_expected))

        with allure.step("Switch to monthly pricing"):
            pricing_page.toggle_billing.click()

        with allure.step("Verify monthly price is shown after toggle"):
            pricing_page.starter_price.should(have.text(started_monthly_expected))