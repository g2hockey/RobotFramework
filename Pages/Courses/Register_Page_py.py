import time
from Base.BasePage import BasePage


class Register_Page_py(BasePage):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'      #Prevent init called twice by RF, needed in every page object IMPORTANT!!
    driver = None

    # Locators
    _review_order = "//h1[contains(text(),'Review Your Order')]"
    _cc_num = "cc_field"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvc"
    _cc_country = "country-select-inside"
    _cc_verify = "verify_cc_btn"

    _course_page = "//a[@class='navbar-brand header-logo']"
    _invalidCreditCard = "//div[@class='payment-errors invalid_number'][contains(text(),'card number is invalid')]"


    def __init__(self):
        super(Register_Page_py,self).__init__(self.driver)

    def setDriver(self, driver):
        self.driver = driver
        print("Register page: " + self.driver.title)


    #Methods for web element
    def enterCardNum(self, num):
        self.sendKeys(num, locator=self._cc_num)

    def enterCardExp(self, exp):
        self.sendKeys(exp, locator=self._cc_exp)

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv)

    def selectCardCountry(self,country):
        self.elementSelect(country,self._cc_country,'id')

    def clickVerifyCardButton(self):
        self.elementClick(locator=self._cc_verify, locatorType='id')
        time.sleep(3)

    def clickCoursesButton(self):
        coursebtn = self.getElement(self._course_page, 'xpath')
        coursebtn.location_once_scrolled_into_view
        coursebtn = self.waitForElementVisible(self._course_page, 'xpath')
        self.elementClick(element=coursebtn)
        time.sleep(3)

    #Method to perform a workflow
    def enterCreditCardInformation(self, num, exp, cvv, country):
        self.waitForElementVisible(self._review_order, 'xpath')
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.selectCardCountry(country)


    def verifyInvalidCreditCard(self):
        messageElement = self.waitForElementVisible(self._invalidCreditCard, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

    def backToCoursePage(self):
        self.clickCoursesButton()



