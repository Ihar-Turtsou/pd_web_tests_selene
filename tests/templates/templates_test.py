import allure
from selene import browser, be, have


@allure.feature("Pricing")
@allure.story("Plans & CTA")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("web", "smoke", "pricing")
@allure.link("https://www.pandadoc.com/pricing/", name="Pricing page")
def test_search_template(setup_browser):
    with allure.step('Open the pricing page'):
        browser.open('/templates/')

    query_text = 'Convertible Note greement Template'

    with allure.step(f'Search for "{query_text}"'):
        browser.element('.input-text.search__input').type(query_text).press_enter()

    with allure.step("Verify search result contains expected title in <p>"):
        browser.all('.card-doc').element_by(have.text(query_text)).should(be.visible)

