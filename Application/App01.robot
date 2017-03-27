*** Settings ***
Documentation    Application workflow
Resource  ../Pages/Home/Login_page.robot
Resource  ../Pages/Home/Navigation_page.robot

Library         Dialogs
Library         String
Library         Collections
Library         ../Pages/Home/Login_Page_py.py
Library         ../Pages/Home/Navigation_Page_py.py
Library         ../Pages/Courses/Courses_Page_py.py
Library         ../Pages/Courses/Register_Page_py.py
Library         ../Utilities/Read_Data.py



*** Keywords ***
LoginWithCredentials
    [ARGUMENTS]     ${email}    ${password}
    Login_page.Click Login Button
    Login_page.Enter Credentials   ${email}      ${password}
    Login_page.Verify Login Successful

IsLoggedIn2
    ${result}=      Navigation_page.IsLoggedIn
    log             ${result}

    Navigation_page.Navigate To Practice
    Navigation_page.Navigate To All Courses
    Navigation_page.Logout


Test method
    Login_page.Show list variable
    get selection from user     Select something        op1     op2     op3
    Pause Execution

Set Driver
    [Arguments]                     ${driver}
    Login_Page_py.setDriver         ${driver}
    Navigation_Page_py.setDriver    ${driver}
    Courses_Page_py.setDriver       ${driver}
    Register_Page_py.setDriver      ${driver}


Test method2

     Login_Page_py.login        test@email.com      abcabc
     ${result}=         Login_Page_py.verifyLoginTitle          Let's Kode It
     SHOULD BE TRUE     ${result}


Test method3
        ${result}=         Navigation_Page_py.isLoggedIn
        SHOULD BE TRUE     ${result}

        Navigation_Page_py.navigateToPractice
        Navigation_Page_py.clickOnAllCourses

Test method4
        Login_Page_py.login        test@email.com      invalid
        ${result}=         Login_Page_py.verifyLoginFailed
        SHOULD BE TRUE     ${result}
        Login_Page_py.clearEmail

        Login_Page_py.login        invalid      invalid
        ${result}=         Login_Page_py.verifyLoginFailed
        SHOULD NOT BE TRUE     ${result}
        Login_Page_py.clearEmail

Test method5
        Login_Page_py.login                 test@email.com      abcabc
        Courses_Page_py.searchCourse        javascript
        Courses_Page_py.clickOnCourse       JavaScript for beginners
        Courses_Page_py.clickOnEnrollButton
        Register_Page_py.enterCreditCardInformation         12345   12/34   123     Canada
        Register_Page_py.clickVerifyCardButton
        ${result}=         Register_Page_py.verifyInvalidCreditCard
        SHOULD BE TRUE     ${result}

        Register_Page_py.backToCoursePage


Test method6
        @{file}     getCSVData      C:/Python_tests/Selenium_tests/Udemy/RobotFramework/Selenium_test/testCourses.csv

        Login_Page_py.login                 test@email.com      abcabc
        :FOR        ${row}     In  @{file}
         \          @{course}=     Convert To List   ${row}
         \          Courses_Page_py.searchCourse        @{course}[0]
         \          BuiltIn.Sleep      1
         \          Courses_Page_py.clickOnCourse       @{course}[0]
         \          Courses_Page_py.clickOnEnrollButton
         \          Register_Page_py.enterCreditCardInformation         @{course}[1]   @{course}[2]   @{course}[3]     @{course}[4]
         \          Register_Page_py.clickVerifyCardButton
         \          ${result}=         Register_Page_py.verifyInvalidCreditCard
         \          SHOULD BE TRUE     ${result}
         \          Register_Page_py.backToCoursePage


Test method7
        Login_Page_py.login                 test@email.com      abcabc
        Courses_Page_py.searchAuthor        Let's Kode It
        Courses_Page_py.searchCategory       Software Testing

Logout
        Navigation_Page_py.logout










