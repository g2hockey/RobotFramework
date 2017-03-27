import time

from Base.BasePage import BasePage


class Courses_Page_py(BasePage):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'      #Prevent init called twice by RF, needed in every page object IMPORTANT!!
    driver = None

    # Locators
    _usericon = "//span[text()='User Settings']"
    _searchcourses_field = "search-courses"
    _course_link = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button"
    _all_courses_link = "All Courses"

    _search_author = "//div[@class='row search']//div[contains(text(),'Author')]//following-sibling::div//button"
    _search_author_select = "//div[contains(text(),'Author')]//following-sibling::div//a[contains(text(),\"{0}\")]"

    _search_category = "//div[@class='row search']//div[contains(text(),'Category')]//following-sibling::div//button"
    _search_category_select = "//div[contains(text(),'Category')]//following-sibling::div//a[contains(text(),\"{0}\")]"

    def __init__(self):
        super(Courses_Page_py,self).__init__(self.driver)


    def setDriver(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        print("courses page: " + self.driver.title)

    #Methods for web element
    def searchCourse(self,courseName):
        searchfield = self.waitForElementVisible(self._searchcourses_field,'id')
        self.clearText(element=searchfield)
        self.sendKeys(courseName, element=searchfield)

    def searchAuthor(self,author):
        self.elementClick(self._search_author,'xpath')
        authorSelection = self.waitForElementVisible(locator=self._search_author_select.format(author), locatorType="xpath")
        self.elementClick(element=authorSelection)
        time.sleep(2)

    def searchCategory(self, category):
        self.elementClick(self._search_category, 'xpath')
        categorySelection = self.waitForElementVisible(locator=self._search_category_select.format(category), locatorType="xpath")
        self.elementClick(element=categorySelection)
        time.sleep(2)

    def clickOnCourse(self,fullCourseName):
        self.elementClick(locator=self._course_link.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        enrollbtn = self.waitForElementVisible(self._enroll_button, 'id')
        enrollbtn.location_once_scrolled_into_view
        self.elementClick(element=enrollbtn)
        time.sleep(3)





