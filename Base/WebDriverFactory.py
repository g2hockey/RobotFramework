"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():


    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """
    driver = ''
    baseURL = 'about:blank'

    def openBrowser(self, browser):
        if browser == "iexplorer":
            # Set ie driver
            # driverLocation = "C:\\Python27\\IEDriverServer.exe"
            # os.environ["webdriver.ie.driver"] = driverLocation
            # driver = webdriver.Ie(driverLocation)
            self.driver = webdriver.Ie()

        elif browser == "firefox":
            profile = self.getFireFoxProfile()
            self.driver = webdriver.Firefox()

        elif browser == "chrome":
            # Set chrome driver
            # driverLocation = "C:\\Python27\\chromedriver.exe"
            # os.environ["webdriver.chrome.driver"] = driverLocation
            # driver = webdriver.Chrome(driverLocation)
            chrome_options = self.getBrowserOptions(browser)
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            profile = self.getFireFoxProfile()
            self.driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        self.driver.implicitly_wait(5)
        # Maximize the window
        self.driver.maximize_window()
        self.driver.get(self.baseURL)



    def gotoURL(self,url):
        self.driver.get(url)

    def getWebDriverInstance(self):
        return self.driver

    def getBrowserOptions(self,browser):
        options = Options()
        if browser == "chrome":

            options.add_experimental_option('prefs', {
                'credentials_enable_service': False,
                'profile': {
                    'password_manager_enabled': False
                }
            })

        return options

    def getFireFoxProfile(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.set_preference('app.update.silent', True)
        # profile.set_preference('app.update.service.enabled', False)
        # profile.set_preference('app.update.staging.enabled', False)

        return profile

    def dismissFireFoxStartupDialog(self, driver):
        #browserName = driver.capabilities["browserName"]
        browserName = driver.name
        print("Browser: " + browserName)
        if browserName == "firefox":
            actions = ActionChains(driver)
            actions.send_keys(Keys.ALT + 'n')
            #actions.perform()


    def closeBrowser(self):
        self.driver.quit()