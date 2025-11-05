"""
HW9 Test Implementation
Implements six test cases for addition and subtraction.
Three test addition, and three test subtraction.
Results are logged in 'test_results.txt'
"""

from datetime import datetime

# --- Program Functions (same as HW5) ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# --- Utility Function to Run Tests ---
def run_test(test_id, description, function, inputs, expected):
    """Executes a test and returns result info."""
    a, b = inputs
    result = function(a, b)
    status = "PASS" if result == expected else "FAIL"
    severity = "N/A" if status == "PASS" else "major"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prepare the output line
    output = (
        f"\nTest Case: {test_id}\n"
        f"Description: {description}\n"
        f"Inputs: {a}, {b}\n"
        f"Expected Result: {expected}\n"
        f"Actual Result: {result}\n"
        f"Status: {status}\n"
        f"Severity: {severity}\n"
        f"Date/Time: {timestamp}\n"
        f"{'-'*50}\n"
    )

    print(output)
    return output


# --- Define the Six Test Cases ---
def main():
    results = []

    # ADDITION TESTS
    results.append(run_test(
        "TC1",
        "Addition of two positive integers",
        add, (5, 7), 12
    ))

    results.append(run_test(
        "TC2",
        "Addition of positive and negative integers",
        add, (10, -3), 7
    ))

    results.append(run_test(
        "TC3",
        "Addition involving zero",
        add, (0, 25), 25
    ))

    # SUBTRACTION TESTS
    results.append(run_test(
        "TC4",
        "Subtraction of two positive integers",
        subtract, (15, 8), 7
    ))

    results.append(run_test(
        "TC5",
        "Subtraction resulting in negative value",
        subtract, (6, 10), -4
    ))

    results.append(run_test(
        "TC6",
        "Subtraction involving zero",
        subtract, (12, 0), 12
    ))

    # --- Write results to a file ---
    with open("test_results.txt", "w") as f:
        f.write("HW9 Test Results Log\n")
        f.write("="*50 + "\n")
        for r in results:
            f.write(r)

    print("✅ All tests executed. Results saved to 'test_results.txt'.")


if __name__ == "__main__":
    main()
