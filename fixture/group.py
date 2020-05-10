from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
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