*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  masa  masatin123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  uusiSalasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  salasananen100
    Output Should Contain  Username has to be at least three characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  masatinä  jokuSalasana1000
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  masa  abc123
    Output Should Contain  Password has to be at least eight characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  masa  pitkäsalasanA
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command