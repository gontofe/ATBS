#! /usr/bin/python3 
# This program detects a strong password
import re, sys


def checkPassword(password):
    lengthre = re.compile(r'\w{8,}')
    mo = lengthre.match(password)
    if mo == None:
        return (False, 'Your password must be at least 8 characters')

    upperre = re.compile(r'^.*[A-Z]+.*$')
    mo2 = upperre.match(password)
    if mo2 == None:
        return (False, '''Your password must contain at
                          least one uppercase character''')

    lowerre = re.compile(r'^.*[a-z]+.*$')
    mo3 = lowerre.match(password)
    if mo3 == None:
        return (False, '''Your password must contain at
                          least one lowercase character''')
    
    return(True, 'Yass queen! Your password is fierce, honey!')


# This would normally be the main body, but I've added 'unit tests' with asserts
"""while True:
    print('please enter a password')
    password = input()
    if password == '':
        print('k thankx byeeeee!')
        sys.exit()
    else:
        response = checkPassword(password)
        print(response)"""

tests = [ ("Test mixed case password", True, "abCD1234"),
          ("Test case no upper", False, "abcd1234"),
          #("Test case she tryna break shit now", True, "a"),
          ("Test case mixed no lower", False, "ABCD1234"),
          ("Test case short password", False, "abC123")]

for test in tests:
    print(test[0] + "\n Expected result: " + str(test[1]) + ", Actual result: ", end = '')
    result, message = checkPassword(test[2])
    print(str(result), end='')
    assert result == test[1], test[0] + " failed! Reason: " + message
    print('. Test passed!')
