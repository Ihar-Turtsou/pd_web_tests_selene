import allure
from selene import browser, be, have, query
from src.pages.pricing_page import PricingPage


@allure.tag("web", "smoke", "pricing")
@allure.feature("Pricing")
@allure.story("Plans & CTA")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.pandadoc.com/pricing/", name="Pricing page")
def test_pricing_plans_cta(setup_browser):
    pricing_page = PricingPage()

    with allure.step('Open the pricing page'):
        pricing_page.pricing_page_open()

    with allure.step("Verify at least 3 pricing plans are displayed"):
        pricing_page.block_of_actual_plans.by(be.visible).should(have.size(3))

    with allure.step("Verify Starter plan CTA leads to trial"):
        pricing_page.button_start_free_trial.click()

        browser.element('h1').should(have.text('Start a free 14-day trial'))


@allure.tag("web", "regression", "pricing")
@allure.feature("Pricing")
@allure.story("Plan price toggle")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://www.pandadoc.com/pricing/", name="Pricing page")
def test_starter_pricing(setup_browser):
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