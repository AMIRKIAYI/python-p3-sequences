#!/usr/bin/env python3

def print_fibonacci(length):
    """Print the first 'length' Fibonacci numbers as a list."""
    a, b = 0, 1
    fibonacci_numbers = []
    for _ in range(length):
        fibonacci_numbers.append(a)
        a, b = b, a + b
    print(fibonacci_numbers)

# Example function calls
print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)
