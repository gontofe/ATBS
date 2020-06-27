#! python3
# regexStrip takes a string and does the same thing as the strip
# string method using regular expressions. If no arguments are passed
# other than the string, whitespace will be removed from the beginning
# and end of the string, otherwise the second argument will be used instead
import re

def regexStrip(inputString, character):
    stripChar = '\\s'
    if character != '':
        stripChar = character
    stripRegex = re.compile(r'^(?:'+ stripChar + r')*(.*?)(?:' + stripChar + r')*$')
    mo = stripRegex.match(inputString)
    return mo.group(1)

testString1 = ' abc123 '
testString2 = '_abc123_'
testString3 = 'badgerabc123badger'
expectedString = 'abc123'

testCases = [ ('perfectly normal strip. ', testString1, ''),
              ('strip with underscore. ', testString2, '_'),
              ('strip with string (badger)', testString3, 'badger')]

for test in testCases:
    try:
        print('Test case: ' + test[0] + ', result: ', end='')
        result = regexStrip(test[1], test[2])
        assert result == expectedString, "oopsie, got " + result
        print(result + ' PASSED')
    except AssertionError as error:
        print("FAILED. Reason: " + str(error))
