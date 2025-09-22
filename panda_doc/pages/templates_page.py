from selene import browser, be, have
import allure


class _TemplatesResults:
    def __init__(self, scope):
        self._cards = scope.all('.card-doc')

    @allure.step('Results should contain: {text}')
    def contains(self, text: str):
        self._cards.element_by(have.text(text)).should(be.visible)


class TemplatesPage:
    search_input = browser.element('.input-text.search__input')

    @allure.step('Open Templates page')
    def open(self):
        browser.open('/templates/')
        return self

    @allure.step('Search for: {query}')
    def search(self, query: str):
        self.search_input.set_value(query).press_enter()
        return self

    @property
    def search_results(self) -> _TemplatesResults:
        return _TemplatesResults(browser)