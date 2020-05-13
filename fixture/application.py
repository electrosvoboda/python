from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

driver = webdriver.Firefox('G:\\Program Files\\geckodriver')


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    @property
    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
