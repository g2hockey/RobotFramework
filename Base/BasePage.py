"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from Base.SeleniumDriver import SeleniumDriver
from traceback import print_stack
from Utilities.Util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):


        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            print("Failed to get page title")
            print_stack()
            return False