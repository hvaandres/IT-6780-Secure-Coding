/*
 * Main Application
 * Demonstrates the use of math library functions
 */

#include <stdio.h>
#include "math_library.h"

void print_result(double num) {
    if (num < 0) {
        printf("(%.0f)", num);
    } else {
        printf("%.0f", num);
    }
}

int main() {
    printf("==================================================\n");
    printf("Math Library Demonstration (C Implementation)\n");
    printf("==================================================\n\n");
    
    // Addition tests
    printf("ADDITION TESTS:\n");
    printf("--------------------------------------------------\n");
    
    double result;
    
    result = add_numbers(7, 3);
    printf("✓ 7 + 3 = %.0f\n", result);
    
    result = add_numbers(18, 73);
    printf("✓ 18 + 73 = %.0f\n", result);
    
    result = add_numbers(-32, 17);
    printf("✓ (-32) + 17 = ");
    print_result(result);
    printf("\n");
    
    printf("\n");
    
    // Subtraction tests
    printf("SUBTRACTION TESTS:\n");
    printf("--------------------------------------------------\n");
    
    result = subtract_numbers(8, 3);
    printf("✓ 8 - 3 = %.0f\n", result);
    
    result = subtract_numbers(-21, -9);
    printf("✓ (-21) - (-9) = ");
    print_result(result);
    printf("\n");
    
    result = subtract_numbers(83, 137);
    printf("✓ 83 - 137 = ");
    print_result(result);
    printf("\n");
    
    printf("\n");
    printf("==================================================\n");
    printf("All tests completed successfully!\n");
    printf("==================================================\n");
    
    return 0;
}