import allure
from selene import be, have
from panda_doc.pages.home_page import HomePage

@allure.tag('web', 'smoke')
@allure.feature('Home')
@allure.story('Header & Footer visibility')
@allure.severity(allure.severity_level.NORMAL)
@allure.link('https://www.pandadoc.com/', name='Homepage')
def test_homepage_header_footer(setup_browser):
    home_page = HomePage()

    with allure.step('Open the homepage'):
        home_page.open()

    with allure.step('Verify logo is visible in the header'):
        home_page.logo.should(be.visible)

    with allure.step('Verify "Prising" menu item is present in the header'):
        home_page.header.should(have.text('Pricing'))

    with allure.step('Verify CTA button is visible and clickable'):
        home_page.cta_free_treal.should(be.visible).should(be.enabled)
        home_page.cta_request_demo.should(be.visible).should(be.enabled)

    with allure.step('Scroll down to the footer'):
        home_page.scroll_to_footer()

    with allure.step('Verify footer is visible'):
        home_page.footer.should(be.visible)

    with allure.step('Verify footer contains key links'):
        home_page.footer.should(have.text('Privacy notice')).should(be.clickable)
        home_page.footer.should(have.text('Legal')).should(be.clickable)