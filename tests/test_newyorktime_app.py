import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

from utils.attachment import add_video


def test_dark_theme():
    with step('Enter to App'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Continue')).click()
    with step('Go to User setting'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, '***')).click()
    with step('Check Dark Theme'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, '***')).click()
    with step('Verify content found'):
        browser.all((AppiumBy.ID, '!!org.wikipedia.alpha:id/page_list_item_title')) \
            .should(have.size_greater_than(0))
    add_video(browser)


def test_nyt_search():
    with step('Press Sections buttom'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, '***')).click()
    with step('Go to search field'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, '***')).click()
    with step('Type search worlds'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Articles')).click()
        browser.element((AppiumBy.ID, "!!org.wikipedia.alpha:id/search_src_text")).type('harry potter')
    with step('Verify content found'):
        browser.all((AppiumBy.ID, '!!org.wikipedia.alpha:id/page_list_item_title')) \
            .should(have.size_greater_than(0))
    add_video(browser)
