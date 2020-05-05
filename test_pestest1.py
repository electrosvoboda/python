# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox('G:\\Program Files\\geckodriver')


class TestPestest1():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}

  
  def test_pestest1(self):
    # Test name: pestest1
    # Step # | name | target | value
    # 1 | open | /addressbook/ | 
    self.driver.get("http://localhost/addressbook/")
    # 2 | setWindowSize | 1936x1056 | 
    self.driver.set_window_size(1936, 1056)
    # 3 | type | name=user | admin
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    # 4 | click | id=content | 
    self.driver.find_element(By.ID, "content").click()
    # 5 | click | name=pass | 
    self.driver.find_element(By.NAME, "pass").send_keys("secret")
    # 6 | click | css=input:nth-child(7) | 
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    # 7 | click | linkText=groups | 
    self.driver.find_element(By.LINK_TEXT, "groups").click()
    # 8 | click | name=new | 
    self.driver.find_element(By.NAME, "new").click()
    # 9 | click | name=group_name | 
    self.driver.find_element(By.NAME, "group_name").click()
    # 10 | type | name=group_name | pes
    self.driver.find_element(By.NAME, "group_name").send_keys("hui")
    # 11 | type | name=group_header | sobaka
    self.driver.find_element(By.NAME, "group_header").send_keys("sobaka")
    # 12 | type | name=group_footer | wtf
    self.driver.find_element(By.NAME, "group_footer").send_keys("wtf")
    # 13 | click | name=submit | 
    self.driver.find_element(By.NAME, "submit").click()
    # 14 | click | linkText=groups | 
    self.driver.find_element(By.LINK_TEXT, "groups").click()
    # 15 | click | linkText=Logout | 
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def teardown_method(self, method):
        self.driver.quit()