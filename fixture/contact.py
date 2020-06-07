from selenium.webdriver.common.by import By
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def changes_field_value(self, field_name, text):
        if text is not None:
            self.driver.find_element(By.NAME, field_name).click()
            self.driver.find_element(By.NAME, field_name).clear()
            self.driver.find_element(By.NAME, field_name).send_keys(text)

    def create(self, contact):
        # create new contact
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "home").click()
        self.driver.find_element(By.NAME, "home").send_keys(contact.homephone)
        self.driver.find_element(By.NAME, "mobile").click()
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobilephone)
        self.driver.find_element(By.NAME, "work").click()
        self.driver.find_element(By.NAME, "work").send_keys(contact.workphone)
        self.driver.find_element(By.NAME, "submit").click()
        self.button_home()

    def button_home(self):
        self.driver.find_element(By.LINK_TEXT, "home").click()

    def select_first_contact(self):
        # select first group
        self.driver.find_element(By.NAME, "selected[]").click()

    def delete_first_contact(self):
        self.button_home()
        self.select_first_contact()
        self.driver.find_element(By.CSS_SELECTOR, "div.left:nth-child(8) > input:nth-child(1)").click()
        # self.driver.find_element(By.LINK_TEXT, "home").click()
        self.driver.find_element(By.ID, "3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
        assert self.driver.switch_to.alert.text == "Delete 1 addresses?"
        self.driver.switch_to.alert.accept()
        self.button_home()

    def select_contact_by_index(self, index):
        self.driver.find_elements(By.NAME, "Edit[]")[index].click()

    def submit_update(self):
        self.driver.find_element(By.LINK_TEXT, "update").click()

    def modify_some_contact(self, index):
        self.button_home()
        self.select_contact_by_index(index)
        self.driver.find_element(By.CSS_SELECTOR, "tr.odd:nth-child(3) > td:nth-child(2)")
        self.submit_update()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.app.open_home_page()
            self.contact_cache = []
            for row in self.driver.find_elements(By.NAME, "entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        self.app.open_home_page()
        row = self.driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        self.app.open_home_page()
        row = self.driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        firstname = self.driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = self.driver.find_element(By.NAME, "lastname").get_attribute("value")
        id = self.driver.find_element(By.NAME, "id").get_attribute("value")
        homephone = self.driver.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = self.driver.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = self.driver.find_element(By.NAME, "work").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone)

    def get_contact_from_view_page(self, index):
        self.open_contact_view_by_index(index)
        text = self.driver.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone)
