from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_groups_page(self):
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

    def select_first_group(self):
        # select first group
        self.driver.find_element(By.NAME, "selected[]").click()

    def delete_first_group(self):
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        self.driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, new_group_data):
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        self.driver.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        # select first group
        self.driver.find_element(By.NAME, "selected[]").click()
