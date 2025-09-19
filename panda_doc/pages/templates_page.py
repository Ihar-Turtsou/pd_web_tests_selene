from selene import browser, have

class TemplatesPage:

    search_input = browser.element('.input-text.search__input')
    cards_doc = browser.all('.card-doc')

    def templates_page_open(self):
        browser.open('/templates/')
        return self