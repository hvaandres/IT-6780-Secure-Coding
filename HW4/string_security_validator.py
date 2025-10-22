import re
import html
import sys

class StringSecurityValidator:
    """Validates strings for safe usage in various contexts"""
    
    def __init__(self):
        # SQL injection patterns
        self.sql_dangerous = [
            r"('|(--)|;|\*|\/\*|\*\/)",  # Common SQL injection chars
            r"\b(DROP|DELETE|INSERT|UPDATE|UNION|EXEC|EXECUTE)\b",  # Dangerous keywords
            r"(xp_|sp_)\w+",  # SQL Server stored procedures
            r"\bOR\b.*=.*",  # OR-based injection
        ]
        
        # XSS patterns for web safety
        self.xss_patterns = [
            r"<script",
            r"javascript:",
            r"onerror\s*=",
            r"onload\s*=",
            r"<iframe",
            r"<embed",
            r"<object",
        ]
        
        # Shell injection patterns
        self.shell_dangerous = [
            r"[;&|`$]",  # Shell command separators and substitution
            r"\$\(",  # Command substitution
            r">\s*/dev",  # Device redirection
            r"\.\./",  # Directory traversal
            r"(rm|del|format)\s+-",  # Dangerous commands
        ]
        
        # Email regex (RFC 5322 simplified)
        self.email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        # ZIP code patterns (US: 5 digits or 5+4, Canada: A1A 1A1)
        self.zip_us = r"^\d{5}(-\d{4})?$"
        self.zip_ca = r"^[A-Z]\d[A-Z]\s?\d[A-Z]\d$"
    
    def is_sql_safe(self, text):
        """Check if string is safe for SQL execution"""
        text_upper = text.upper()
        
        # Check for dangerous patterns
        for pattern in self.sql_dangerous:
            if re.search(pattern, text_upper, re.IGNORECASE):
                return False
        
        # Check for multiple statements
        if text.count(';') > 0:
            return False
        
        return True
    
    def is_web_safe(self, text):
        """Check if string is safe to display in a web browser"""
        text_lower = text.lower()
        
        # Check for XSS patterns
        for pattern in self.xss_patterns:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return False
        
        # Check for HTML event handlers
        if re.search(r"on\w+\s*=", text_lower):
            return False
        
        return True
    
    def is_shell_safe(self, text):
        """Check if string is safe to execute as a shell command"""
        # Check for dangerous patterns
        for pattern in self.shell_dangerous:
            if re.search(pattern, text):
                return False
        
        # Check for newlines (command chaining)
        if '\n' in text or '\r' in text:
            return False
        
        return True
    
    def is_valid_email(self, text):
        """Check if string is a valid email address"""
        text = text.strip()
        
        if not re.match(self.email_pattern, text):
            return False
        
        # Additional validation
        if text.count('@') != 1:
            return False
        
        local, domain = text.split('@')
        
        # Check length constraints
        if len(local) > 64 or len(domain) > 255:
            return False
        
        # Check for consecutive dots
        if '..' in text:
            return False
        
        return True
    
    def is_valid_zipcode(self, text):
        """Check if string is a valid ZIP code (US or Canadian)"""
        text = text.strip()
        
        # Check US ZIP code
        if re.match(self.zip_us, text):
            return True
        
        # Check Canadian postal code
        if re.match(self.zip_ca, text, re.IGNORECASE):
            return True
        
        return False
    
    def get_safe_alternatives(self, text):
        """Suggest safe alternatives for unsafe strings"""
        suggestions = []
        
        if not self.is_sql_safe(text):
            # Escape single quotes for SQL
            escaped = text.replace("'", "''")
            suggestions.append(f"SQL-safe: Use parameterized query with value: {escaped}")
        
        if not self.is_web_safe(text):
            # HTML escape
            escaped = html.escape(text)
            suggestions.append(f"Web-safe: {escaped}")
        
        if not self.is_shell_safe(text):
            suggestions.append("Shell-safe: Use proper escaping or avoid shell execution")
        
        return suggestions
    
    def validate_string(self, text, line_num=None):
        """Validate a string against all criteria"""
        prefix = f"Line {line_num}: " if line_num else ""
        
        results = {
            'text': text[:50] + '...' if len(text) > 50 else text,
            'sql_safe': self.is_sql_safe(text),
            'web_safe': self.is_web_safe(text),
            'shell_safe': self.is_shell_safe(text),
            'valid_email': self.is_valid_email(text),
            'valid_zipcode': self.is_valid_zipcode(text)
        }
        
        return results

def process_file(filename):
    """Process a text file and validate each line"""
    validator = StringSecurityValidator()
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print(f"{'='*80}")
        print(f"STRING SECURITY VALIDATION REPORT")
        print(f"File: {filename}")
        print(f"Total lines: {len(lines)}")
        print(f"{'='*80}\n")
        
        for i, line in enumerate(lines, 1):
            line = line.rstrip('\n\r')
            
            if not line.strip():  # Skip empty lines
                continue
            
            results = validator.validate_string(line, i)
            
            print(f"Line {i}: {results['text']}")
            print(f"  SQL Safe:        {'✓ YES' if results['sql_safe'] else '✗ NO'}")
            print(f"  Web Safe:        {'✓ YES' if results['web_safe'] else '✗ NO'}")
            print(f"  Shell Safe:      {'✓ YES' if results['shell_safe'] else '✗ NO'}")
            print(f"  Valid Email:     {'✓ YES' if results['valid_email'] else '✗ NO'}")
            print(f"  Valid ZIP Code:  {'✓ YES' if results['valid_zipcode'] else '✗ NO'}")
            
            # Show suggestions for unsafe strings
            if not all([results['sql_safe'], results['web_safe'], results['shell_safe']]):
                suggestions = validator.get_safe_alternatives(line)
                if suggestions:
                    print(f"  Suggestions:")
                    for suggestion in suggestions:
                        print(f"    - {suggestion}")
            
            print()
        
        print(f"{'='*80}")
        print("Validation complete!")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        print("\nExample test strings:")
        print("  - SELECT * FROM users")
        print("  - <script>alert('XSS')</script>")
        print("  - rm -rf /")
        print("  - user@example.com")
        print("  - 12345")
        print("\nCreate a text file with one string per line and run the validator.")
        return
    
    filename = sys.argv[1]
    process_file(filename)

if __name__ == "__main__":
    main()