#import utilities.custom_logger as cl
import logging
import time
from Base.BasePage import BasePage

class Navigation_Page_py(BasePage):

    #log = cl.CustomLogger(logging.DEBUG)

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'      #Prevent init called twice by RF, needed in every page object IMPORTANT!!
    driver = None

    # Locators
    _my_courses = "My Courses"
    _practice = "Practice"
    _usericon = "//span[text()='User Settings']"
    _all_courses_link = "All Courses"
    _logout = "Log out"

    def __init__(self):
        print("navgiation init")
        super(Navigation_Page_py,self).__init__(self.driver)


    def setDriver(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        print("navigation page: " + self.driver.title)

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="partial_link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="partial_link")
        time.sleep(3)

    def navigateToUserSettings(self):
        self.elementClick(locator=self._usericon, locatorType="xpath")

    def clickLogout(self):
        logoutBtn = self.waitForElementVisible(self._logout, 'partial_link')
        self.elementClick(element=logoutBtn)

    def clickOnAllCourses(self):
        allCourseBtn = self.getElement(self._all_courses_link,'partial_link')
        allCourseBtn.location_once_scrolled_into_view
        self.elementClick(element=allCourseBtn)
        time.sleep(3)

    def isLoggedIn(self):
        return self.isElementPresent(self._usericon,locatorType="xpath")

    def logout(self):
        if self.isLoggedIn():
            self.navigateToUserSettings()
            self.clickLogout()
            time.sleep(3)
