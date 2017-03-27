from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
#import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver(object):

    #log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        # type: (object) -> object
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else:
            print ("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def elementSelect(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)

            select = Select(element)
            select.select_by_visible_text(data)

            print("Selected option on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot select on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)

            if element is not None:
                print("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                print("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElementVisible(self, locator, locatorType="id",
                               timeout=15, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, 15, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType,locator)))
            print("Element appeared on the web page: " + locator)
        except Exception as ex:
            print("Element not appeared on the web page: " + locator)
            print_stack()

        return element

    def getTitle(self):
        return self.driver.title

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def webScroll(self, direction="up" ):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                if isDisplayed:
                    print("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
                else:
                    print("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                print("Element not found")

            return isDisplayed
        except:
            print("Element not found")
            return False

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def clearText(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.clear()
            print("Clear text on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot clear text on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()