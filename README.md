# Codsoft_Taskno_1_Simple_Calculator

# Simple Calculator - Python

## Project Overview

This project is a *Simple Calculator* written in *Python*, designed as part of an internship task for *CodSoft*. It performs basic arithmetic operations like:

- Addition
- Subtraction 
- Multiplication  
- Division

It interacts with the user via the command line, prompting for input numbers and the type of operation to be performed.

---

## Features

- Accepts user input for two numbers
- Prompts the user to select an arithmetic operation
- Performs the calculation
- Handles invalid input gracefully
- Displays the result of the operation

---

## How It Works

1. The program starts by printing a welcome message and operation menu.
2. The user is prompted to enter two numeric values.
3. Then, the user selects an operation from the menu (`+`, `-`, `*`, `/`).
4. Based on the selection, the corresponding arithmetic function is called.
5. The result is displayed in a formatted output.
6. If the user provides invalid input (e.g., division by zero or wrong operator), the program handles it using error handling mechanisms like try-except blocks.

---

## Files Included

- `calculator.py` – The main script file containing the implementation.
- `README.md` – This documentation file explaining the purpose and usage of the calculator.

---

## Example Output

```bash
Welcome to the Simple Calculator!
Enter first number: 10
Enter second number: 5
Choose operation (+, -, *, /): *

Result: 10.0 * 5.0 = 50.0
