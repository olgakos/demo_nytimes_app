import os
import pytest
from dotenv import load_dotenv
from appium import webdriver
from datetime import date

from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """
    Load .env
    """
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def app_android():
    """
    Create driver
    """
    USER = os.getenv('LOGIN')
    KEY = os.getenv('KEY')
    APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')

    desired_cap = {
        "app": "bs://0e73cacaa99b3e3085b1aa1533521c6a24df4de0", #2022-12-20
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "platformName": "android",
        "project": "Python NYT project",
        "build": "browserstack-build-" + str(date.today()),
        'bstack:options': {
            "projectName": "Python NYT project",
            "buildName": "browserstack-build-NYT",
            "sessionName": "BStack test"
        }
    }
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{USER}:{KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )
    browser.config.timeout = 4
    yield app_android
    browser.quit()