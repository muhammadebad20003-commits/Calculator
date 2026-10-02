# Basic Calculator with Execution Time Measurement

## Introduction

This project is a basic calculator developed in Python for the Parallel and Distributed Computing course.

The calculator performs basic arithmetic operations and measures the execution time of each operation using Python's `time.perf_counter()` function.

## Features

The calculator supports the following operations:

* Addition
* Subtraction
* Multiplication
* Division
* Division-by-zero error handling
* Execution time measurement
* Simple command-line interface

## Technologies Used

* Python 3
* Python `time` module

## Project Structure

```text
parallel-calculator/
│
├── calculator.py
└── README.md
```

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```


## How Execution Time is Measured

The program uses Python's `time.perf_counter()` function.

The timer starts immediately before the arithmetic operation:

```python
start_time = time.perf_counter()
```

After the operation is completed, the timer stops:

```python
end_time = time.perf_counter()
```

The execution time is calculated as:

```python
execution_time = end_time - start_time
```

This gives the time taken by the operation in seconds.

## Sample Output

```text
========================================
       BASIC PYTHON CALCULATOR
========================================

Select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice: 1
Enter first number: 50
Enter second number: 25

Result: 75.0
Execution Time: 0.0000012000 seconds
```


## Purpose

The main purpose of this project is to understand basic computation and observe the execution time of different arithmetic operations. This provides a simple introduction to performance measurement, which is relevant to Parallel and Distributed Computing.

## Author

Muhammad Ebad

## License

This project is created for educational purposes.
