*** Settings ***
Documentation    Suite description

Variables  test_vars
Library  ../send_api_request/api_request.py

*** Test Cases ***
1. Create Gist
    [Tags]
    ${Response} =  api_request.send_request

