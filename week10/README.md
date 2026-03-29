# Simple Python Calculator

## 📘 Overview
This project is a basic command-line calculator built in Python.  
It allows users to perform four fundamental arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division

## ✨ Features
- Interactive menu for selecting operations.
- Accepts two numeric inputs from the user.
- Uses a custom `math_tools` module for calculations.
- Displays the result of the chosen operation.

## ⚙️ Requirements
- Python 3.x
- A `math_tools.py` file containing:
  ```python
  def add(a, b): return a + b
  def subtract(a, b): return a - b
  def multiply(a, b): return a * b
  def divide(a, b): return a / b if b != 0 else "Error: Division by zero"
  ```

## Usage
1. Clone or download this repository.

2. Ensure you have Python installed (python --version).

3. Run the script:
```python3 main.py
```

4. Follow the prompts:

  - Select an operation (1–4).

  - Enter two numbers.

  - View the result.

```
    Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    Enter choice (1/2/3/4): 1
    Enter first number: 10
    Enter second number: 5

    Result: 15.0
```

   
