*** Settings ***
Documentation    Navigation bar
Library         Selenium2Library

*** Variables ***
${NAVIGATION_PAGE_MY_COURSES}       My Courses
${NAVIGATION_PAGE_PRACTICE}         Practice
${NAVIGATION_PAGE_ALL_COURSES}      All Courses
${NAVIGATION_PAGE_LOG_OUT}          //a[contains(text(),'Log out')]
${NAVIGATION_PAGE_USERICON}         //span[text()='User Settings']


*** Keywords ***
Navigate To My Courses
    click element  partial link=${NAVIGATION_PAGE_MY_COURSES}
    sleep   5

Navigate To All Courses
    wait until element is visible   partial link=${NAVIGATION_PAGE_ALL_COURSES}     timeout=10
    click element  partial link=${NAVIGATION_PAGE_ALL_COURSES}
    sleep   5


Navigate To Practice
    wait until element is visible   partial link=${NAVIGATION_PAGE_PRACTICE}     timeout=10
    click element  partial link=${NAVIGATION_PAGE_PRACTICE}
    sleep   5


Navigate To UserSettings
    click element  xpath=${NAVIGATION_PAGE_USERICON}

ClickLogout
    click element  xpath=${NAVIGATION_PAGE_LOG_OUT}

Logout
    Navigate To UserSettings
    wait until element is visible   xpath=${NAVIGATION_PAGE_LOG_OUT}     timeout=10
    ClickLogout


IsLoggedIn
    wait until element is visible   xpath=${NAVIGATION_PAGE_USERICON}     timeout=10
    ${result}=      run keyword and return status       page should contain element     xpath=${NAVIGATION_PAGE_USERICON}
    [Return]        ${result}



