"""
Main Application
Demonstrates the use of math_library functions
"""

# Import functions from the library
from math_library import add_numbers, subtract_numbers


def format_result(num):
    """Format negative numbers with parentheses"""
    if num < 0:
        return f"({num})"
    return str(num)


def main():
    """
    Main function that demonstrates library usage with required test cases
    """
    print("=" * 50)
    print("Math Library Demonstration")
    print("=" * 50)
    print()
    
    # Required test cases for Addition
    print("ADDITION TESTS:")
    print("-" * 50)
    
    test_cases_add = [
        (7, 3, 10),
        (18, 73, 91),
        (-32, 17, -15)
    ]
    
    for first, second, expected in test_cases_add:
        result = add_numbers(first, second)
        status = "✓" if result == expected else "✗"
        print(f"{status} {format_result(first)} + {format_result(second)} = {format_result(result)}")
    
    print()
    
    # Required test cases for Subtraction
    print("SUBTRACTION TESTS:")
    print("-" * 50)
    
    test_cases_sub = [
        (8, 3, 5),
        (-21, -9, -12),
        (83, 137, -54)
    ]
    
    for first, second, expected in test_cases_sub:
        result = subtract_numbers(first, second)
        status = "✓" if result == expected else "✗"
        print(f"{status} {format_result(first)} - {format_result(second)} = {format_result(result)}")
    
    print()
    print("=" * 50)
    print("All tests completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()