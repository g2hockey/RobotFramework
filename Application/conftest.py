
from selenium import webdriver
from Base.WebDriverFactory import WebDriverFactory
#from pages.home.login_page import LoginPage
from robot.libraries.BuiltIn import BuiltIn

class conftest():

    driver2 = ''

    # def __init__(self):
    #     self.driver = None

    def oneTimeSetup(self, browser="firefox"):
        print("Running one time setUp")
        # wdf = WebDriverFactory(browser)
        # driver = wdf.getWebDriverInstance()
        # self.driver2 = driver


    def oneTimeTearDown(self):
        # print("suite tear down: " + self.driver2.title)
        # self.driver2.quit()
        print("Running one time tearDown")

    def setUpTest(self):
        print("Running method level setUp")


    def tearDownTest(self):
        print("Running method level setUp")

        print("Running method level tearDown")

    def get_webdriver_instance(self):
        se2lib = BuiltIn().get_library_instance('Selenium2Library')
        driver = se2lib._current_browser()
        return driver