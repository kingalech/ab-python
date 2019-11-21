# Imports
import sys
import os

from nose.tools import assert_true, assert_is_not_none, assert_is
from selenium import webdriver


# Browser Definition
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('--headless')

# Web driver Path Declaration
browser = webdriver.Chrome(
    executable_path=r'/usr/local/lib/python2.7/site-packages/selenium/webdriver/chrome/chromedriver',
    chrome_options=options)


# Environment Variable Declaration
url = os.environ['URL']
email = os.environ['EMAIL']
password = os.environ['PASSWORD']

# Expected Texts
exp_login_title = 'Login | Dream Team'
exp_dashboard_title = 'Dashboard | Dream Team'
exp_logout_msg = 'You have successfully been logged out.'


# Automation Execution
def test_open_url():
    """URL should be browsed in Chrome browser."""
    browser.get(url)
    return assert_is_not_none(browser.title)


def test_open_login_page():
    """Login Page should load."""
    login_page_link = browser.find_element_by_link_text('Login')
    login_page_link.click()
    login_title = str(browser.title)
    assert exp_login_title == login_title


def test_login():
    """User must be login with correct username and password."""
    input_username = browser.find_element_by_id('email')
    input_username.send_keys(email)

    input_password = browser.find_element_by_id('password')
    input_password.send_keys(password)

    btn_login = browser.find_element_by_id("submit")
    btn_login.click()

    dashboard_title = browser.title
    assert exp_dashboard_title == dashboard_title


def test_dashboard():
    """Dashboard must get open with hostname"""
    dashboard_caption = browser.find_element_by_xpath('//h3[starts-with(text(),"The page is being served from")]')
    return assert_is_not_none(dashboard_caption.text)


def test_logout():
    logout = browser.find_element_by_link_text('Logout')
    logout.click()

    logout_confirmation = browser.find_element_by_xpath('//div[@class="alert alert-info"]')
    logout_msg = str(logout_confirmation.text)
    browser.close()
    assert exp_logout_msg == logout_msg

