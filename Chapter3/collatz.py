def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(str(result))
        return result
    else:
        result = 3 * number + 1
        print(str(result))
        return result

print('Enter number:')
try:
    number = int(input())
    result = collatz(number)
    while result != 1:
        result = collatz(result)
except ValueError:
    print('You must enter an integer')
