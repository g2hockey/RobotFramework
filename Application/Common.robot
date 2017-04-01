*** Settings ***
Documentation    Keywords for Common methods
Library  Selenium2Library
Library     ../Base/WebDriverFactory.py


*** Variables ***
${COMMON_Browser}      firefox          #chrome       #iexplorer       #firefox
${COMMON_TEST_URL}     https://letskodeit.teachable.com
${COMMON_WEBDRIVER}                            #Global webdriver object to pass into Page Object classes

*** Keywords ***
Setup Testsuite
    Open Webpage
    ${COMMON_WEBDRIVER}=   WebDriverFactory.getWebDriverInstance
    set suite variable      ${COMMON_WEBDRIVER}
    log             webdriver: ${COMMON_WEBDRIVER}


Teardown Testsuite
    Close webpage

Setup Test
    Log     Test setup

Teardown Test
    log     Test teardown

Open Webpage
    WebDriverFactory.openBrowser        ${COMMON_Browser}
    WebDriverFactory.gotoURL            ${COMMON_TEST_URL}

Close webpage
    WebDriverFactory.closeBrowser



