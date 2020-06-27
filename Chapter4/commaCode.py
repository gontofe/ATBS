def listify(list):
    returnString = ''
    for i in range(len(list) ):
        if i != len(list) - 1:
            returnString += list[i] + ', '
        else:
            returnString += 'and ' + list[i]
    return returnString

spam = ['apples', 'bananas', 'tofu', 'cats']
print(listify(spam))
