import allure
from selene import browser, be, have, query


@allure.feature("Pricing")
@allure.story("Plans & CTA")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("web", "smoke", "pricing")
@allure.link("https://www.pandadoc.com/pricing/", name="Pricing page")
def test_pricing_plans_cta(setup_browser):
    with allure.step('Open the pricing page'):
        browser.open('/pricing/')

    with allure.step("Verify at least 3 pricing plans are displayed"):
        browser.element('.grid-plan--3').all('.grid-plan__item').by(be.visible).should(have.size(3))

    with allure.step("Verify Starter plan CTA leads to trial"):
        browser.element('[data-testid="pd-button-start-free-trial"]').click()
        browser.element('h1').should(have.text('Start a free 14-day trial'))

@allure.feature("Pricing")
@allure.story("Plans choosing")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("web", "smoke", "pricing")
@allure.link("https://www.pandadoc.com/pricing/", name="Pricing page")
def test_starter_pricing(setup_browser):
    with allure.step('Open the pricing page'):
        browser.open('/pricing/')

    starter_price_element = browser.element('[data-personalization-plan="starter"] .plan__amount')

    with allure.step("Get expected values from attributes"):
       started_annual_expected = starter_price_element.get(query.attribute('data-toggleable-original'))
       started_monthly_expected = starter_price_element.get(query.attribute('data-toggleable-alternative'))

    with allure.step("Verify annual price is shown by default"):
        starter_price_element.should(have.text(started_annual_expected))

    with allure.step("Switch to monthly pricing"):
        browser.element('[data-testid="pd-block-pricing"] .toggler__toggle.toggler__toggle--accent').click()

    with allure.step("Verify monthly price is shown after toggle"):
        starter_price_element.should(have.text(started_monthly_expected))