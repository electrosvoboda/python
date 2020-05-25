from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def create(self, contact):
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
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.LINK_TEXT, "home").click()

    def select_first_contact(self):
        # select first group
        self.driver.find_element(By.NAME, "selected[]").click()

    def delete_first_contact(self):
        self.driver.find_element(By.LINK_TEXT, "home").click()
        self.select_first_contact()
        self.driver.find_element(By.CSS_SELECTOR, "div.left:nth-child(8) > input:nth-child(1)").click()
        #self.driver.find_element(By.LINK_TEXT, "home").click()
        self.driver.find_element(By.ID, "3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
        assert self.driver.switch_to.alert.text == "Delete 1 addresses?"
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "home").click()

