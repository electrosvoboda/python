from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def login(self, username, password):
        # login addressbook
        self.app.open_home_page()
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.ID, "content").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
