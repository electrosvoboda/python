from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

driver = webdriver.Firefox('G:\\Program Files\\geckodriver')


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()