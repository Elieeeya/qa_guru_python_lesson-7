import allure
from selene import by, be
from selene.support.shared.jquery_style import s, ss
from conftest import *


def test_decorator_steps():
    open_main_page()
    finding_repository('eroshenkoam/allure-example')
    follow_link_repository('eroshenkoam/allure-example')
    open_issues_tab()
    checking_number('76')




@allure.step('Opening the main page')
def open_main_page():
    browser.open("https://github.com")


@allure.step('Finding a repository {repo}')
def finding_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Follow the link of the repository {repo}')
def follow_link_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Open the issues tab')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step('Checking line number 76')
def checking_number(number):
    s(by.partial_text('#' + number)).should(be.visible)
