import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

from utils.attachment import add_video


def test_dark_theme():
    with step('Enter to App'):
        browser.element((AppiumBy.LINK_TEXT, 'Continue')).click()
    with step('Go to User setting (Icon)'):
        #browser.element((AppiumBy.ACCESSIBILITY_ID, 'com.nytimes.android:id/touch_outside')).click()
        #browser.element((AppiumBy.ACCESSIBILITY_ID, 'android.widget.Button')).click()
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.Button')).click();
    with step('Chek Button Theme'):
        # text Theme
        browser.element((AppiumBy.LINK_TEXT, 'Theme')).click()
    with step('Check Dark Theme'):
        #text Dark
        #browser.element((AppiumBy.ACCESSIBILITY_ID, '**')).click()
        #browser.element((AppiumBy.LINK_TEXT, 'Dark')).click()
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')).click();
        #By.xpath("//android.widget.TextView[contains(@text, 'Dark')]");
    '''
    with step('Verify content found'):
        browser.all((AppiumBy.ID, 'com.nytimes.android:id/touch_outside')) \
            .should(have.size_greater_than(0))
    '''
    add_video(browser)


def test_nyt_search():
    with step('Press Sections buttom'):
        browser.element((AppiumBy.LINK_TEXT, 'Sections')).click()
    with step('Go to search field'):
        #browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).click()
   #OR
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Articles')).click()
    with step('Type search worlds'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Articles')).type('harry potter')
    with step('Verify content found'):
        browser.all((AppiumBy.PARTIAL_LINK_TEXT, 'Tom Felton Auditioned for ‘Harry Potter’ Without Reading the Books')) \
            .should(have.size_greater_than(0))
    add_video(browser)
