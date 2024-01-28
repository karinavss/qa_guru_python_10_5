import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 750
    browser.config.window_height = 1500


    yield

    browser.quit()
