import allure
from selene import browser, be, have

@allure.tag('smoke')
@allure.feature('Homepage')
@allure.story('Header & Footer visibility')
def test_homepage_header_footer(setup_browser):
    with allure.step('Open the homepage'):
        browser.open('/')

    with allure.step('Verify logo is visible in the header'):
        browser.element('.logo').should(be.visible)

    with allure.step('Verify "Prising" menu item is present in the header'):
        browser.element('header').should(have.text('Pricing'))

    with allure.step('Verify CTA button is visible and clickable'):
        browser.element('[data-testid="pd-button-start-free-trial"]').should(be.visible).should(be.enabled)
        browser.element('[data-testid="pd-button-request-demo"]').should(be.visible).should(be.enabled)

    with allure.step('Scroll down to the footer'):
        pass