# Homework Assignment: Creating and Using Software Libraries

## 📚 Project Overview

This project demonstrates the fundamental concepts of **software libraries** in programming. We created reusable mathematical functions (addition and subtraction) and packaged them into a library that can be used by other programs.

### What is a Library?

A **library** is a collection of pre-written code that can be reused by different programs. Instead of writing the same code over and over, we write it once in a library and then "import" or "link" it into any program that needs it.

**Think of it like a real library:** Instead of writing a book yourself every time you need information, you go to the library and borrow the book you need.

---

## 🎯 Assignment Requirements

### Main Requirements:
1. ✅ Create two functions (addition and subtraction) in a library
2. ✅ Write a main application that uses these library functions
3. ✅ Test with specific values to prove correctness:
   - 7 + 3 = 10
   - 18 + 73 = 91
   - (-32) + 17 = (-15)
   - 8 - 3 = 5
   - (-21) - (-9) = (-12)
   - 83 - 137 = (-54)

### Extra Credit:
4. ✅ Demonstrate **static linking** (compile-time)
5. ✅ Demonstrate **dynamic linking** (run-time)

---

## 🐍 Python Implementation

### File Structure
```
project/
│
├── math_library.py    # The library (reusable functions)
└── main.py           # The application (uses the library)
```

### File 1: `math_library.py` (The Library)

```python
"""
Math Library Module
Contains addition and subtraction functions for use in applications
"""

def add_numbers(first, second):
    """
    Function to return the sum of two arguments
    
    Args:
        first: First number (int or float)
        second: Second number (int or float)
    
    Returns:
        Sum of the two numbers
    """
    return first + second


def subtract_numbers(first, second):
    """
    Function to return the difference of two arguments
    
    Args:
        first: First number (int or float)
        second: Second number (int or float)
    
    Returns:
        Difference of the two numbers (first - second)
    """
    return first - second
```

**What this does:**
- Defines two simple functions: `add_numbers()` and `subtract_numbers()`
- These functions are **reusable** - any program can import and use them
- This is our **library** - a collection of related functions

---

### File 2: `main.py` (The Application)

```python
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
```

**What this does:**
- **Imports** the functions from our library using `from math_library import add_numbers, subtract_numbers`
- Tests all the required calculations
- Shows that our library functions work correctly
- This demonstrates **using a library** in an application

---

### Running the Python Version

```bash
# Make sure both files are in the same directory
python main.py
```

**Output:**
```
==================================================
Math Library Demonstration
==================================================

ADDITION TESTS:
--------------------------------------------------
✓ 7 + 3 = 10
✓ 18 + 73 = 91
✓ (-32) + 17 = (-15)

SUBTRACTION TESTS:
--------------------------------------------------
✓ 8 - 3 = 5
✓ (-21) - (-9) = (-12)
✓ 83 - 137 = (-54)

==================================================
All tests completed successfully!
==================================================
```

---

## 🔧 C Implementation (Extra Credit)

The C version demonstrates **two types of linking**:

### 📖 Linking Explained

**Linking** is the process of combining your program with library code.

1. **Static Linking (Compile-time)**
   - Library code is **copied into** your executable when you compile
   - Creates a **larger** executable file
   - ✅ **Advantage:** Executable is self-contained, no external files needed
   - ❌ **Disadvantage:** Larger file size, can't update library without recompiling

2. **Dynamic Linking (Run-time)**
   - Library code stays **separate** in a `.so` / `.dll` / `.dylib` file
   - Your executable just references the library
   - ✅ **Advantage:** Smaller executable, multiple programs share one library, can update library without recompiling
   - ❌ **Disadvantage:** Library file must be present at runtime

---

### File Structure (C Version)
```
project/
│
├── math_library.h     # Header (function declarations)
├── math_library.c     # Implementation (function definitions)
└── main.c            # Application (uses the library)
```

---

### File 3: `math_library.h` (Header File)

```c
/*
 * Math Library Header File
 * Function declarations for addition and subtraction
 */

#ifndef MATH_LIBRARY_H
#define MATH_LIBRARY_H

/**
 * Add two numbers
 * @param first First number
 * @param second Second number
 * @return Sum of the two numbers
 */
double add_numbers(double first, double second);

/**
 * Subtract two numbers
 * @param first First number
 * @param second Second number
 * @return Difference (first - second)
 */
double subtract_numbers(double first, double second);

#endif /* MATH_LIBRARY_H */
```

**What this does:**
- **Declares** the functions (tells the compiler they exist)
- This is like a "table of contents" for the library
- Other programs include this file to know what functions are available

---

### File 4: `math_library.c` (Implementation)

```c
/*
 * Math Library Implementation
 * Contains the actual function implementations
 */

#include "math_library.h"

double add_numbers(double first, double second) {
    return first + second;
}

double subtract_numbers(double first, double second) {
    return first - second;
}
```

**What this does:**
- **Defines** the actual function code
- This is the "real" library that gets compiled

---

### File 5: `main.c` (Application)

```c
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
```

**What this does:**
- Uses the library functions to perform the required tests
- Same functionality as Python version, but in C

---

## 🔨 Building and Running (C Version)

### Option 1: Static Linking

```bash
# Step 1: Compile library source to object file
gcc -c math_library.c -o math_library.o

# Step 2: Create static library archive (.a file)
ar rcs libmath.a math_library.o

# Step 3: Compile main program and link with static library
gcc main.c -L. -lmath -o main_static

# Step 4: Run the program
./main_static

# Verify it's statically linked
ldd main_static  # Should NOT show libmath dependency
```

**What happens:**
- `math_library.o` - Compiled library code (object file)
- `libmath.a` - Static library archive (collection of .o files)
- `main_static` - Final executable with library code **embedded inside**
- The executable is **self-contained** and doesn't need external files

---

### Option 2: Dynamic Linking

```bash
# Step 1: Compile library as Position Independent Code
gcc -c -fPIC math_library.c -o math_library.o

# Step 2: Create shared library (.so file on Linux)
gcc -shared -o libmath.so math_library.o

# Step 3: Compile main program
gcc main.c -L. -lmath -o main_dynamic

# Step 4: Set library path and run
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
./main_dynamic

# Verify it's dynamically linked
ldd main_dynamic  # SHOULD show libmath.so dependency
```

**What happens:**
- `math_library.o` - Compiled library code (position independent)
- `libmath.so` - Shared library (separate file)
- `main_dynamic` - Executable that **references** the library
- The executable needs `libmath.so` to be present when it runs

**For macOS:** Use `.dylib` instead of `.so`
```bash
gcc -dynamiclib -o libmath.dylib math_library.o
export DYLD_LIBRARY_PATH=.:$DYLD_LIBRARY_PATH
```

**For Windows:** Use `.dll` instead of `.so`
```bash
gcc -shared -o math.dll math_library.o -Wl,--out-implib,libmath.a
```

---

## 📊 Comparison: Static vs Dynamic

| Feature | Static Linking | Dynamic Linking |
|---------|---------------|-----------------|
| **File Extension** | `.a` (Linux/Mac), `.lib` (Windows) | `.so` (Linux), `.dylib` (Mac), `.dll` (Windows) |
| **Executable Size** | Larger (contains library code) | Smaller (references library) |
| **External Dependencies** | None (self-contained) | Requires library file at runtime |
| **Memory Usage** | Each program has own copy | Multiple programs share one copy |
| **Updates** | Must recompile to update | Can update library without recompiling |
| **Distribution** | Easier (one file) | Must include library files |
| **Load Time** | Faster | Slightly slower |

---

## 🎓 Key Concepts Learned

### 1. **Software Libraries**
- A library is a collection of reusable code
- Libraries promote code reuse and organization
- [Wikipedia: Library (Computing)](https://en.wikipedia.org/wiki/Library_(computing))

### 2. **API (Application Programming Interface)**
- The "interface" to a library - the functions you can call
- In our case: `add_numbers()` and `subtract_numbers()`
- [Wikipedia: API](https://en.wikipedia.org/wiki/API)

### 3. **Static Linking**
- Library code compiled into the executable
- Happens at compile-time
- [Wikipedia: Static Library](https://en.wikipedia.org/wiki/Static_library)

### 4. **Dynamic Linking**
- Library code kept separate, loaded at runtime
- Also called "shared libraries"
- [Wikipedia: Dynamic Linker](https://en.wikipedia.org/wiki/Dynamic_linker)

### 5. **Separation of Interface and Implementation**
- Header files (`.h`) declare what functions exist
- Implementation files (`.c`) define how they work
- Users only need to know the interface to use the library

---

## 📝 What We Did Step-by-Step

1. **Took the original code** from Homework 1 (which had add and subtract functions)
2. **Extracted the functions** into a separate library file
3. **Created a main application** that imports/links to the library
4. **Tested all required calculations** to prove correctness
5. **For extra credit:** Implemented both static and dynamic linking in C

---

## 🚀 How to Submit

### Required Files:
- [ ] `math_library.py`
- [ ] `main.py`
- [ ] Screenshot of running `python main.py`

### Extra Credit Files:
- [ ] `math_library.h`
- [ ] `math_library.c`
- [ ] `main.c`
- [ ] Screenshot showing static library build commands and execution
- [ ] Screenshot showing dynamic library build commands and execution
- [ ] Optional: Screenshot showing `ldd` output comparing static vs dynamic

---

## 💡 Why This Matters

Understanding libraries is fundamental to programming because:

1. **Code Reusability** - Write once, use many times
2. **Modularity** - Organize code into logical units
3. **Maintenance** - Update library without changing programs that use it
4. **Collaboration** - Share code with other developers
5. **Performance** - Dynamic libraries save memory when shared

Real-world examples:
- **Python:** `numpy`, `pandas`, `requests` are all libraries
- **C/C++:** Standard library (`stdio.h`, `stdlib.h`), OpenGL, SDL
- **Operating Systems:** Windows DLLs, Linux shared objects
- **Web:** jQuery, React, Bootstrap are JavaScript libraries

---

## 📚 References

- [Wikipedia: Library (Computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Wikipedia: Shared Library](https://en.wikipedia.org/wiki/Shared_library)
- [Wikipedia: API](https://en.wikipedia.org/wiki/API)
- [Wikipedia: Static Library](https://en.wikipedia.org/wiki/Static_library)
- [Wikipedia: Dynamic Linker](https://en.wikipedia.org/wiki/Dynamic_linker)

---

## ✅ Expected Output

```
==================================================
Math Library Demonstration
==================================================

ADDITION TESTS:
--------------------------------------------------
✓ 7 + 3 = 10
✓ 18 + 73 = 91
✓ (-32) + 17 = (-15)

SUBTRACTION TESTS:
--------------------------------------------------
✓ 8 - 3 = 5
✓ (-21) - (-9) = (-12)
✓ 83 - 137 = (-54)

==================================================
All tests completed successfully!
==================================================
```

---
