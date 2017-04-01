#import utilities.custom_logger as cl
import logging
import time
from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Base.BasePage import BasePage

class Practice_Page_py(BasePage):

    #log = cl.CustomLogger(logging.DEBUG)

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'      #Prevent init called twice by RF, needed in every page object IMPORTANT!!
    driver = None

    # Locators
    _radio_benz = "//div[@id='radio-btn-example']//input[@id='benzradio']"
    _checkbox_honda = "//div[@id='checkbox-example']//input[@id='hondacheck']"
    _select_car = "//select[@id='carselect']"
    _newWindow = "//button[@id='openwindow']"
    _newTab = "//a[@id='opentab']"
    _alert = "//input[@id='alertbtn']"
    _confirm = "//input[@id='confirmbtn']"
    _table = "//table[@id='product']"

    def __init__(self):
        print("Practice init")
        super(Practice_Page_py,self).__init__(self.driver)

    def setDriver(self, driver):
        self.driver = driver
        print("Practice page: " + self.driver.title)

    def selectRadioBtn(self):
        self.elementClick(locator=self._radio_benz, locatorType="xpath")

    def selectDropBox(self, data):
        self.elementSelect(data, locator=self._select_car,locatorType='xpath')

    def selectCheckbox(self):
        self.elementClick(locator=self._checkbox_honda, locatorType='xpath')

    def switchWindow(self):
        parenthandle = self.driver.current_window_handle

        self.elementClick(locator=self._newWindow,locatorType="xpath")

        allwindows = self.driver.window_handles

        for handle in allwindows:
            print("window: " + handle)
            if handle != parenthandle:
                self.driver.switch_to.window(handle)
                print ("New window: " +self.driver.title + " handle: " + handle)
                time.sleep(3)
                self.driver.close()


        self.driver.switch_to.window(parenthandle)

    def switchTab(self):
        parenthandle = self.driver.current_window_handle

        self.elementClick(locator=self._newTab, locatorType="xpath")
        time.sleep(5)

        allwindows = self.driver.window_handles
        self.driver.switch_to.window(allwindows[0])
        time.sleep(5)
        self.driver.switch_to.window(allwindows[1])
        time.sleep(5)
        self.driver.close()

        self.driver.switch_to.window(parenthandle)

    def switchAlert(self):

        self.elementClick(locator=self._alert,locatorType="xpath")
        time.sleep(2)

        alert = self.driver.switch_to.alert
        print("Alert text: " + alert.text)
        alert.accept()
        time.sleep(2)

        self.elementClick(locator=self._confirm, locatorType="xpath")
        time.sleep(2)

        confirm = self.driver.switch_to.alert
        print("Confirm text: " + confirm.text)
        confirm.dismiss()
        time.sleep(2)


    def showTable(self):
        table = self.getElement(locator=self._table,locatorType="xpath")
        table.location_once_scrolled_into_view

        rows = table.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for i in range(len(rows)):
            row_data = ""
            cols = ""
            if i == 0:
                cols = rows[i].find_elements(By.TAG_NAME, "th")
            else:
                cols = rows[i].find_elements(By.TAG_NAME, "td")

            for data in cols:
                row_data += data.text +" "

            print(row_data)


    def mousehover(self):
        element = self.getElement(locator="//button[@id='mousehover']",locatorType="xpath")
        #element.location_once_scrolled_into_view
        time.sleep(3)

        #actions.move_to_element throws exceptions in Firefox, ok in Chrome
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            itemToClickLocator = "//div[@class ='mouse-hover']//a[text()='Top']"
            #reloadBtn = self.waitForElementVisible(locator=itemToClickLocator,locatorType="xpath")
            #reloadBtn.location_once_scrolled_into_view
            reloadBtn = self.getElement(locator=itemToClickLocator,locatorType="xpath")
            actions.move_to_element(reloadBtn).click().perform()
            print("Item Clicked")
            time.sleep(2)
        except:
            print("Mouse Hover failed on element")
            print_stack()


    def mousehover2(self):
        element = self.getElement(locator="//button[@id='mousehover']",locatorType="xpath")
        element.location_once_scrolled_into_view
        time.sleep(3)

        #actions.move_to_element throws exceptions in Firefox, ok in Chrome
        self.hoverButton(element=element)
        time.sleep(3)

        itemToClickLocator = "//div[@class ='mouse-hover']//a[text()='Top']"
        self.hoverButtonClick(locator=itemToClickLocator,locatorType="xpath")
        time.sleep(2)
