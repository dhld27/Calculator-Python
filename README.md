# Calculator-Python
this program creates a basic calculator application with addition, subtraction, multiplication, and division functions.


#Basic Calculator Application
##Description
This program is a simple calculator application that allows users to perform basic arithmetic operations. The available functions are:

- Addition
- Subtraction
- Multiplication
- Division


# Features
- Addition: Adds two numbers.
- Subtraction: Subtracts the second number from the first number.
- Multiplication: Multiplies two numbers.
- Division: Divides the first number by the second number.

# Requirements
Python 3.x

# Installation
***Clone the repository:***

```
git clone https://github.com/yourusername/basic-calculator.git
```

***Navigate to the project directory:***

```
cd basic-calculator
```

***Run the calculator script:***

```
python calculator.py
```

***Usage***  
Once the program is running, follow the prompts to perform calculations. You will be asked to:

1. Pick an option  
2. Choose the operation (Addition, Subtraction, Multiplication, Division).  
3. Enter the first and second number (exception for `division`, when the second number is null the program will ask to input a number > 0).  
4. The program will ask to input another number after doing the first operations  
5. The program will then display the result of the operation including how many inputs has been done.  

*Example*
```
Simple Calculator in Python!
              Enter 'a' for Addition
              Enter 's' for Subtraction
              Enter 'm' for Multiplication
              Enter 'd' for Division
              Enter 'q' to quit
```

*When doing an arithmetic operations: Addition*
```
Addition
Enter a number: 2
Enter another number: 3
Current result: 5.0
Enter more (y/n): y
Enter another number: 1
Current result: 6.0
Enter more (y/n): n
Answer = 6.0 and the total inputs: 3
```
# Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch `(git checkout -b feature-branch)`.
3. Commit your changes `(git commit -am 'Add new feature')`.
4. Push to the branch `(git push origin feature-branch)`.
5. Create a new Pull Request.


# Acknowledgments
This application was inspired by the need for a simple, command-line based calculator.
