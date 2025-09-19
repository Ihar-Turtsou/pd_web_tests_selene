from selene import browser, have

class PricingPage:

    # block_of_actual_plans = browser.element('.grid-plan--3').all('.grid-plan__item')
    button_start_free_trial = browser.element('[data-testid="pd-button-start-free-trial"]')
    toggle_billing = browser.element('[data-testid="pd-block-pricing"] .toggler__toggle.toggler__toggle--accent')

    starter_price = browser.element('[data-personalization-plan="starter"] .plan__amount')

    def pricing_page_open(self):
        browser.open('/pricing/')
        return self


