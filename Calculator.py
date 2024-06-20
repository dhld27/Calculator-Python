import os 
def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    continueCalc = 'y'

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    answer = num1 + num2
    valuesEntered = 2
    print(f'Current result: {answer}')

    while continueCalc.lower() == 'y':
        continueCalc = (input('Enter more (y/n): '))
        while continueCalc.lower() not in ['y', 'n']:
            print("Please enter \'y\' or \'n'")
            continueCalc = (input('Enter more (y/n): '))

        if continueCalc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        answer += num
        print(f'Current result: {answer}')
        valuesEntered += 1
    return [answer, valuesEntered]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    continueCalc = 'y'

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    answer = num1 - num2
    valuesEntered = 2
    print(f'Current result: {answer}')

    while continueCalc.lower() == 'y':
        continueCalc = (input('Enter more (y/n): '))
        while continueCalc.lower() not in ['y', 'n']:
            print("Please enter \'y\' or \'n\'")
            continueCalc = (input('Enter more (y/n): '))
        
        if continueCalc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        answer -= num
        print(f'Current result: {answer}')
        valuesEntered += 1
    return[answer, valuesEntered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multipilcation')

    continueCalc = 'y'

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    answer = num1 * num2
    valuesEntered = 2
    print(f'Current result: {answer}')

    while continueCalc.lower() == 'y':
        continueCalc = (input('Enter more(y/n): '))
        while continueCalc.lower() not in ['y', 'n']:
            print("Please enter \'y\' or \'n\'")
            continueCalc = (input('Enter more (y/n): '))

        if continueCalc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        answer *= num
        print(f'Current result: {answer}')
        valuesEntered += 1
    return [answer, valuesEntered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Division')

    continueCalc = 'y'

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    while num2 == 0.0:
        print('Please enter a second number more than 0!')
        num2 = float(input('Enter a number more than 0: '))
    answer = num1 / num2
    valuesEntered = 2
    print(f'Current result: {answer}')
    
    while continueCalc.lower() == 'y':
        continueCalc = (input('Enter more(y/n): '))
        while continueCalc.lower() not in ['y', 'n']:
            print("Please enter \'y\' or \'n\'")
            continueCalc = (input('Enter more(y/n): '))

        if continueCalc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        while num == 0.0:
            print('Please enter a number more than 0!')
            num = float(input('Enter another number: '))
        answer /= num
        print(f'Current result: {answer}')
        valuesEntered += 1
    return [answer, valuesEntered]

def calculator():
    quit = False
    while not quit:
        results = []
        print('''
            Simple Calculator in Python!
              Enter \'a\' for Addition
              Enter \'s\' for Subtraction
              Enter \'m\' for Multiplication
              Enter \'d\' for Division
              Enter \'q\' to quit
              ''')
        choice = input('Selection: ')
        if choice == 'q':
            quit = True
            print('Thank you for using the Calculator!')
        
            continue

        if choice == 'a':
            results = addition()
            print(f'Answer = {results[0]} and the total inputs: {results[1]}')
        elif choice == 's':
            results = subtraction()
            print(f'Answer = {results[0]} and the total inputs: {results[1]}')
        elif choice == 'm':
            results = multiplication()
            print(f'Answer = {results[0]} and the total inputs: {results[1]}')
        elif choice == 'd':
            results = division()
            print(f'Answer = {results[0]} and the total inputs: {results[1]}')
        else: 
            print('Invalid character')

if __name__ == '__main__':
    calculator()