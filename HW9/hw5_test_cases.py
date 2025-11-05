import unittest

# --- HW5 Program Logic (Example Implementation) ---
# You can replace this later with your actual HW5 functions.

def add(a, b):
    """Performs addition of two numbers."""
    return a + b

def subtract(a, b):
    """Performs subtraction of two numbers."""
    return a - b


# --- Unit Test Cases for Addition and Subtraction ---
class TestHW5MathOperations(unittest.TestCase):

    # ---------- ADDITION TEST CASES ----------
    def test_add_two_positive_integers(self):
        """Test Case #1: Addition of two positive integers"""
        result = add(5, 7)
        self.assertEqual(result, 12, "5 + 7 should equal 12")

    def test_add_positive_and_negative_integers(self):
        """Test Case #2: Addition of positive and negative integers"""
        result = add(10, -3)
        self.assertEqual(result, 7, "10 + (-3) should equal 7")

    def test_addition_with_zero(self):
        """Test Case #3: Addition involving zero"""
        result = add(0, 25)
        self.assertEqual(result, 25, "0 + 25 should equal 25")

    # ---------- SUBTRACTION TEST CASES ----------
    def test_subtract_two_positive_integers(self):
        """Test Case #4: Subtraction of two positive integers"""
        result = subtract(15, 8)
        self.assertEqual(result, 7, "15 - 8 should equal 7")

    def test_subtraction_resulting_in_negative_value(self):
        """Test Case #5: Subtraction resulting in a negative result"""
        result = subtract(6, 10)
        self.assertEqual(result, -4, "6 - 10 should equal -4")

    def test_subtraction_with_zero(self):
        """Test Case #6: Subtraction involving zero"""
        result = subtract(12, 0)
        self.assertEqual(result, 12, "12 - 0 should equal 12")


# --- Run the tests when the file is executed ---
if __name__ == '__main__':
    unittest.main()
