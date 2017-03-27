*** Settings ***
Documentation    Login page workflow
Library         Selenium2Library

*** Variables ***
${LOGIN_PAGE_LOGIN}            Login
${LOGIN_PAGE_USER_EMAIL}       user_email
${LOGIN_PAGE_USER_PASSWORD}    user_password
${LOGIN_PAGE_COMMIT}           commit
${LOGIN_PAGE_USERICON}         //span[text()='User Settings']
@{MY_List}                      data1   data2   data3


*** Keywords ***
Click Login Button
    wait until element is visible   partial link=${LOGIN_PAGE_LOGIN}      timeout=10
    click element  partial link=${LOGIN_PAGE_LOGIN}

Enter "Email" Field
    [ARGUMENTS]     ${email}
    input text  id=${LOGIN_PAGE_USER_EMAIL}     ${email}

Enter "Password" Field
    [ARGUMENTS]     ${password}
    input password  id=${LOGIN_PAGE_USER_PASSWORD}  ${password}

Enter Credentials
    [ARGUMENTS]     ${email}    ${password}
    wait until element is visible   id=${LOGIN_PAGE_USER_EMAIL}       timeout=10
    Enter "Email" Field             ${email}
    Enter "Password" Field          ${password}
    click element  name=${LOGIN_PAGE_COMMIT}

Verify Login Successful
    wait until element is visible  xpath=${LOGIN_PAGE_USERICON}    timeout=10
    page should contain element  xpath=${LOGIN_PAGE_USERICON}


Show list variable
    log  @{MY_List}[0]
    log  @{MY_List}[1]
    log  @{MY_List}[2]
    ${my_method_var}       set variable  my variable
    @{my_method_list}       create list  my data 1      my data 2  my data 3

    run keyword and continue on failure  wait until page contains  No such text
    log     My method var: ${my_method_var}
    log     My method list: ${my_method_list}
