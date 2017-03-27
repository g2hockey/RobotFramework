*** Settings ***
Documentation    Keywords for Common methods
Library  Selenium2Library
Library     ../Application/conftest.py
Library     ../Utilities/Util.py


*** Variables ***
${COMMON_Browser}      firefox          #chrome       #Ie       #firefox
${COMMON_TEST_URL}     https://letskodeit.teachable.com
${WEBDRIVER}                            #Global webdriver object to pass into Page Object classes

*** Keywords ***
Setup Testsuite
    Open Webpage
    ${WEBDRIVER}=   Util.Get webdriver instance
    set suite variable      ${WEBDRIVER}
    log             webdriver: ${webdriver}


Teardown Testsuite
    Close webpage

Setup Test
    Log     Test setup

Teardown Test
    log     Test teardown

Open Webpage
    open browser    about:blank   ${COMMON_Browser}
    maximize browser window
    go to   ${COMMON_TEST_URL}

Close webpage
    close browser



