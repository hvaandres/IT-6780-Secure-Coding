# String Security Validator

## Description
A Python program that reads a text file and validates each line for security and formatting issues across five different contexts.

## What It Does
Tests each string to determine if it's safe to:
1. Execute as SQL or save to a database
2. Display in a web browser (XSS protection)
3. Execute as a shell command
4. Use as an email address (format validation)
5. Use as a ZIP code (US or Canadian format)

## Installation
```bash
# No dependencies required - uses Python standard library only
python --version  # Requires Python 3.6+
```

## Usage
```bash
python string_validator.py test_data.txt
```

## Input Format
Create a text file with one string per line:
```text
Hello World
user@example.com
SELECT * FROM users
<script>alert('XSS')</script>
rm -rf /
12345
```

## Output
```
Line 1: Hello World
  SQL Safe:        ✓ YES
  Web Safe:        ✓ YES
  Shell Safe:      ✓ YES
  Valid Email:     ✗ NO
  Valid ZIP Code:  ✗ NO
```

## Detection Capabilities

### SQL Injection
- Dangerous keywords (DROP, DELETE, UNION)
- SQL comments and special characters
- Multiple statement attempts

### XSS Attacks
- Script tags and JavaScript
- HTML event handlers
- Dangerous HTML elements (iframe, embed)

### Shell Injection
- Command separators (;, |, &, `)
- Command substitution
- Directory traversal
- Dangerous commands

### Email Validation
- RFC 5322 format (user@domain.tld)
- Length constraints
- Special character rules

### ZIP Code Validation
- US: 12345 or 12345-6789
- Canadian: A1A 1A1

## Files
- `string_validator.py` - Main program
- `test_data.txt` - Test cases (70+ examples)
- `README.md` - This file

## Note
This is an educational tool. In production, always use parameterized queries, input sanitization libraries, and proper security frameworks.