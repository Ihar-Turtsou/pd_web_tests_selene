import allure
import pytest

@allure.tag("web", "smoke", "templates")
@allure.feature("Templates")
@allure.story("Search")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.pandadoc.com/templates/", name="Templates page")
@pytest.mark.parametrize('query_text', ['Convertible Note Agreement Template'])
def test_search_template(setup_browser, templates_page, query_text):
    templates_page.open().search(query_text)
    templates_page.search_results.contains(query_text)

