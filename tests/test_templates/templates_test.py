import allure
from selene import browser, be, have
from panda_doc.pages.templates_page import TemplatesPage


@allure.tag("web", "smoke", "templates")
@allure.feature("Templates")
@allure.story("Search")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.pandadoc.com/templates/", name="Templates page")
def test_search_template(setup_browser):
    templates_page = TemplatesPage()
    query_text = 'Convertible Note Agreement Template'

    with allure.step('Open the pricing page'):
        templates_page.templates_page_open()

    with allure.step(f'Search for "{query_text}"'):
        templates_page.search_input.type(query_text).press_enter()

    with allure.step("Verify search result contains expected title in <p>"):
        templates_page.cards_doc.element_by(have.text(query_text)).should(be.visible)

