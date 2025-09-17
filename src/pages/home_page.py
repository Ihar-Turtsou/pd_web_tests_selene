from selene import browser, have


class HomePage:

    logo = browser.element('.logo')
    header = browser.element('header')
    cta_free_treal = browser.element('[data-testid="pd-button-start-free-trial"]')
    cta_request_demo = browser.element('[data-testid="pd-button-request-demo"]')
    footer = browser.element('footer')


    def home_page_open(self):
        browser.open('')
        return self

    def scroll_to_footer(self):
        browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self
