from selene import browser


class RequestDemoPage:

    email_input = browser.element('[name="email"]')
    submit_button = browser.element('[data-testid="pd-button-submit-form"]')

    email_error = browser.element(".hs-form-field.hs_email .hs-error-msg")
    phone_error = browser.element(".hs-form-field.hs_phone .hs-error-msg")

    def open(self):
        browser.open("/getdemo/")
        return self

