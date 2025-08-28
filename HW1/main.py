import hashlib
import json
from decimal import Decimal, getcontext
from typing import Union

# Set decimal precision for consistent calculations
getcontext().prec = 50

def validate_input(value) -> Union[Decimal, None]:
    """
    Validates and converts input to Decimal for precise calculations
    """
    try:
        if isinstance(value, (int, float, str)):
            return Decimal(str(value))
        elif isinstance(value, Decimal):
            return value
        else:
            return None
    except (ValueError, TypeError, OverflowError):
        return None

def generate_operation_hash(first, second, operation):
    """
    Generates a hash for the operation to ensure consistency
    """
    operation_data = {
        'first': str(first),
        'second': str(second),
        'operation': operation,
        'precision': getcontext().prec
    }
    operation_string = json.dumps(operation_data, sort_keys=True)
    return hashlib.sha256(operation_string.encode()).hexdigest()[:8]

def add_numbers(first, second):
    """
    Secure function to return the sum of two arguments
    """
    validated_first = validate_input(first)
    validated_second = validate_input(second)
    
    if validated_first is None or validated_second is None:
        raise ValueError("Invalid input parameters")
    
    result = validated_first + validated_second
    operation_hash = generate_operation_hash(validated_first, validated_second, 'add')
    
    if result == result.to_integral_value():
        display_result = int(result)
    else:
        display_result = float(result)
    
    return display_result, operation_hash

def subtract_numbers(first, second):
    """
    Secure function to return the difference of two arguments
    """
    validated_first = validate_input(first)
    validated_second = validate_input(second)
    
    if validated_first is None or validated_second is None:
        raise ValueError("Invalid input parameters")
    
    result = validated_first - validated_second
    operation_hash = generate_operation_hash(validated_first, validated_second, 'subtract')
    
    if result == result.to_integral_value():
        display_result = int(result)
    else:
        display_result = float(result)
    
    return display_result, operation_hash

def multiply_numbers(first, second):
    """
    Secure function to return the product of two arguments
    """
    validated_first = validate_input(first)
    validated_second = validate_input(second)
    
    if validated_first is None or validated_second is None:
        raise ValueError("Invalid input parameters")
    
    result = validated_first * validated_second
    operation_hash = generate_operation_hash(validated_first, validated_second, 'multiply')
    
    if result == result.to_integral_value():
        display_result = int(result)
    else:
        display_result = float(result)
    
    return display_result, operation_hash

def run_test_scenarios():
    """
    Run predefined test scenarios to verify calculations
    """
    print("Running Test Scenarios...")
    print("-" * 30)
    
    # Test cases
    addition_tests = [(2, 5, 7), (37, 57, 94), (-19, 41, 22)]
    subtraction_tests = [(20, 7, 13), (8, 26, -18), (270, 157, 113)]
    
    # Addition tests
    for first, second, expected in addition_tests:
        result, hash_val = add_numbers(first, second)
        status = "✓" if result == expected else "✗"
        print(f"{status} {first} + {second} = {result}")
    
    # Subtraction tests
    for first, second, expected in subtraction_tests:
        result, hash_val = subtract_numbers(first, second)
        status = "✓" if result == expected else "✗"
        print(f"{status} {first} - {second} = {result}")
    
    print("Test scenarios completed.\n")

def get_user_input():
    """
    Get user input for interactive calculations
    """
    while True:
        try:
            print("Enter two numbers for calculation:")
            first = input("First number: ")
            second = input("Second number: ")
            
            # Validate inputs
            if validate_input(first) is None:
                print("Invalid first number. Please try again.\n")
                continue
            if validate_input(second) is None:
                print("Invalid second number. Please try again.\n")
                continue
            
            # Get operation choice
            print("\nChoose operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (×)")
            choice = input("Enter choice (1, 2, or 3): ")
            
            if choice not in ['1', '2', '3']:
                print("Invalid choice. Please enter 1, 2, or 3.\n")
                continue
            
            return float(first), float(second), choice
            
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            return None, None, None
        except Exception:
            print("Invalid input. Please try again.\n")

def interactive_calculator():
    """
    Interactive calculator mode
    """
    print("Interactive Calculator Mode")
    print("-" * 30)
    
    while True:
        first, second, choice = get_user_input()
        
        if first is None:  # User interrupted
            break
            
        try:
            if choice == '1':
                result, hash_val = add_numbers(first, second)
                operation = "+"
            elif choice == '2':
                result, hash_val = subtract_numbers(first, second)
                operation = "-"
            else:  # choice == '3'
                result, hash_val = multiply_numbers(first, second)
                operation = "×"
            
            print(f"\nResult: {first} {operation} {second} = {result}")
            print(f"Hash: {hash_val}")
            
        except Exception as e:
            print(f"Error: {e}")
        
        # Ask if user wants to continue
        print("\nContinue? (y/n): ", end="")
        if input().lower() != 'y':
            break
        print()

def main():
    """
    Main function with menu system
    """
    print("Secure Calculator")
    print("=" * 30)
    
    while True:
        print("\nChoose mode:")
        print("1. Run test scenarios")
        print("2. Interactive calculator")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            print()
            run_test_scenarios()
        elif choice == '2':
            print()
            interactive_calculator()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()