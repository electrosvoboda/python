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

    def is_logged_in(self):
        return len(self.driver.find_elements_by_link_text("Logout")) > 0

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in_as(self, username):
        return self.driver.find_element_by_xpath('//div/div[1]/form/b').text == "(" + username + ")"

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
