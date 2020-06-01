from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_home_page(self):
        self.driver.find_element(By.LINK_TEXT, "home").click()

    def open_groups_page(self):
        if not (self.driver.current_url.endswith("/group.php") and len(self.driver.find_elements(By.NAME, "new")) > 0):
            self.driver.find_element(By.LINK_TEXT, "groups").click()

    def changes_field_value(self, field_name, text):
        if text is not None:
            self.driver.find_element(By.NAME, field_name).click()
            self.driver.find_element(By.NAME, field_name).clear()
            self.driver.find_element(By.NAME, field_name).send_keys(text)

    def fill_group_form(self, group):
        self.changes_field_value("group_name", group.name)
        self.changes_field_value("group_header", group.header)
        self.changes_field_value("group_footer", group.footer)

    def create(self, group):
        self.open_groups_page()
        # init new group creation
        self.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        # select first group
        self.driver.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        # select first group
        self.driver.find_elements(By.NAME, "selected[]")[index].click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        self.driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        self.driver.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        # select first group

    def count(self):
        self.open_groups_page()
        return len(self.driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in self.driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
