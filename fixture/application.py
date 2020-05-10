from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

from fixture.session import SessionHelper

driver = webdriver.Firefox('G:\\Program Files\\geckodriver')


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.open_groups_page()
        # init new group creation
        self.driver.find_element(By.NAME, "new").click()
        # fill group firm
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()



    def destroy(self):
        self.driver.quit()

    def create_new_contact(self, contact):
        # create new contact
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "middlename").click()
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "nickname").click()
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "company").click()
        self.driver.find_element(By.NAME, "company").send_keys(contact.mesto_raboti)
        self.driver.find_element(By.NAME, "address").click()
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "home").click()
        self.driver.find_element(By.NAME, "home").send_keys(contact.home_phone)
        self.driver.find_element(By.NAME, "mobile").click()
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        # self.driver.find_element(By.NAME, "bday").click()
        # dropdown = self.driver.find_element(By.NAME, "bday")
        # dropdown.find_element(By.XPATH, "//option[. = '9']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(11)").click()
        # self.driver.find_element(By.NAME, "bmonth").click()
        # dropdown = self.driver.find_element(By.NAME, "bmonth")
        # dropdown.find_element(By.XPATH, "//option[. = 'May']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(6)").click()
        # self.driver.find_element(By.NAME, "byear").click()
        # self.driver.find_element(By.NAME, "byear").send_keys("1945")
        # self.driver.find_element(By.NAME, "address2").click()
        # self.driver.find_element(By.NAME, "new_group").click()
        # dropdown = self.driver.find_element(By.NAME, "new_group")
        # dropdown.find_element(By.XPATH, "//option[. = 'pes']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(14)").click()
        # self.driver.find_element(By.NAME, "theform").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.driver.find_element(By.LINK_TEXT, "home").click()