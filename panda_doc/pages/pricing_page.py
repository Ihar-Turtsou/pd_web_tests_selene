from selene import browser, have, query
import allure


class PricingPage:


    button_start_free_trial = browser.element('[data-testid="pd-button-start-free-trial"]')
    toggle_billing = browser.element('[data-testid="pd-block-pricing"] .toggler__toggle.toggler__toggle--accent')
    starter_price = browser.element('[data-personalization-plan="starter"] .plan__amount')

    @allure.step('Open the pricing page')
    def open(self):
        browser.open('/pricing/')
        return self

    @allure.step("Verify Starter plan CTA leads to trial")
    def start_free_trial(self):
        self.button_start_free_trial.click()
        return self

    @allure.step("Read expected Starter prices from data attributes")
    def read_expected_starter_prises(self):
        annual = self.starter_price.get(query.attribute('data-toggleable-original'))
        monthly = self.starter_price.get(query.attribute('data-toggleable-alternative'))
        return annual, monthly

    @allure.step("Switch to monthly pricing")
    def switch_billing_toggle(self):
        self.toggle_billing.click()
        return self