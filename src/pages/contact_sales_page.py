from selene import browser, be

class ContactSalesPage:

    submit_button = browser.element('[data-testid="pd-button-submit-form"]')
    company_error = browser.element(".hs-form-field.hs_company .hs-error-msg")


    def open_sales(self):
        browser.open("/contact-sales/")
        return self

    def close_cookies_if_visible(self):
        cookie_btn = browser.element(".onetrust-close-btn-handler")
        if cookie_btn.matching(be.visible):
            cookie_btn.click()
        return self

