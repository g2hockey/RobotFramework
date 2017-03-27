import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
from Base.BasePage import BasePage
from Application.conftest   import conftest


class Login_Page_py(BasePage):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'      #Prevent init called twice by RF, needed in every page object IMPORTANT!!
    driver = None

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _usericon = "//span[text()='User Settings']"
    _invalidinput = "//*[@id='new_user']//div[contains(text(),'Invalid email or password')]"



    def __init__(self):
        print("login init")
        super(Login_Page_py, self).__init__(self.driver)

    def setDriver(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        print("login page: " + self.driver.title)

    def click_login_link(self):
        self.elementClick(self._login_link, locatorType="partial_link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='id')

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType='id')

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def clearEmail(self):
        self.clearText(self._email_field, locatorType='id')

    def login(self, email="", password=""):
        self.waitForElementVisible(self._login_link, locatorType="partial_link")
        self.click_login_link()

        self.waitForElementVisible(self._email_field, locatorType='id')
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)

    def verifyLoginTitle(self, title):
        return self.verifyPageTitle(title)

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._invalidinput, locatorType='xpath')
        return result