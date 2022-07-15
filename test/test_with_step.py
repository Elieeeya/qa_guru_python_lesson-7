import allure
from selene import by, be
from selene.support.shared.jquery_style import s, ss
from conftest import *


def test_github(browser_size):
    with allure.step('Opening the main page'):
        browser.open("https://github.com")

    with allure.step('Finding a repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step('Follow the link of the repository'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Open the issues tab'):
        s("#issues-tab").click()

    with allure.step('Checking line number 76'):
        s(by.partial_text("#76")).should(be.visible)

