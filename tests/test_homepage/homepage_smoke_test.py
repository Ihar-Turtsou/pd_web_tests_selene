import allure
from selene import be, have


@allure.tag('web', 'smoke')
@allure.feature('Home')
@allure.story('User authorisation')
@allure.severity(allure.severity_level.BLOCKER)
@allure.link('https://www.pandadoc.com/', name='Homepage')
def test_homepage_log_in(setup_browser, home_page):

    with allure.step('Open the homepage'):
        home_page.open()
# Log_in test will be adding later....