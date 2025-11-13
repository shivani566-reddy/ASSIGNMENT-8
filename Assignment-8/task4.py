import unittest
from typing import Union

def assign_grade(score: Union[int, float]) -> str:

    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


class TestAssignGrade(unittest.TestCase):
    # A range
    def test_A_upper(self):
        self.assertEqual(assign_grade(100), "A")

    def test_A_lower(self):
        self.assertEqual(assign_grade(90), "A")

    # B range
    def test_B_upper(self):
        self.assertEqual(assign_grade(89), "B")

    def test_B_lower(self):
        self.assertEqual(assign_grade(80), "B")

    # C range
    def test_C_upper(self):
        self.assertEqual(assign_grade(79), "C")

    def test_C_lower(self):
        self.assertEqual(assign_grade(70), "C")

    # D range
    def test_D_upper(self):
        self.assertEqual(assign_grade(69), "D")

    def test_D_lower(self):
        self.assertEqual(assign_grade(60), "D")

    # F range
    def test_F_boundary(self):
        self.assertEqual(assign_grade(59), "F")

    def test_zero(self):
        self.assertEqual(assign_grade(0), "F")

    # Float handling near boundaries
    def test_float_near_boundaries(self):
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(59.999), "F")
        self.assertEqual(assign_grade(90.0), "A")
        self.assertEqual(assign_grade(79.999), "C")

    # Invalid inputs: out of range
    def test_negative_score_raises(self):
        with self.assertRaises(ValueError):
            assign_grade(-5)

    def test_too_large_score_raises(self):
        with self.assertRaises(ValueError):
            assign_grade(105)

    # Invalid inputs: wrong type
    def test_string_input_raises(self):
        with self.assertRaises(TypeError):
            assign_grade("eighty")

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            assign_grade(None)

    def test_list_input_raises(self):
        with self.assertRaises(TypeError):
            assign_grade([85])

if __name__ == "__main__":
    unittest.main()
# filepath: c:\Users\madad\OneDrive\Desktop\AIAP\Assignment-8\task2.py
import unittest
from typing import Union

def assign_grade(score: Union[int, float]) -> str:
    """
    Assign a letter grade based on numeric score.
    Rules:
      90-100 -> 'A'
      80-89  -> 'B'
      70-79  -> 'C'
      60-69  -> 'D'
      <60    -> 'F'
    Accepts int or float. Raises TypeError for non-numeric inputs and
    ValueError for scores outside 0-100.
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


class TestAssignGrade(unittest.TestCase):
    # A range
    def test_A_upper(self):
        self.assertEqual(assign_grade(100), "A")

    def test_A_lower(self):
        self.assertEqual(assign_grade(90), "A")

    # B range
    def test_B_upper(self):
        self.assertEqual(assign_grade(89), "B")

    def test_B_lower(self):
        self.assertEqual(assign_grade(80), "B")

    # C range
    def test_C_upper(self):
        self.assertEqual(assign_grade(79), "C")

    def test_C_lower(self):
        self.assertEqual(assign_grade(70), "C")

    # D range
    def test_D_upper(self):
        self.assertEqual(assign_grade(69), "D")

    def test_D_lower(self):
        self.assertEqual(assign_grade(60), "D")

    # F range
    def test_F_boundary(self):
        self.assertEqual(assign_grade(59), "F")

    def test_zero(self):
        self.assertEqual(assign_grade(0), "F")

    # Float handling near boundaries
    def test_float_near_boundaries(self):
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(59.999), "F")
        self.assertEqual(assign_grade(90.0), "A")
        self.assertEqual(assign_grade(79.999), "C")

    # Invalid inputs: out of range
    def test_negative_score_raises(self):
        with self.assertRaises(ValueError):
            assign_grade(-5)

    def test_too_large_score_raises(self):
        with self.assertRaises(ValueError):
            assign_grade(105)

    # Invalid inputs: wrong type
    def test_string_input_raises(self):
        with self.assertRaises(TypeError):
            assign_grade("eighty")

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            assign_grade(None)

    def test_list_input_raises(self):
        with self.assertRaises(TypeError):
            assign_grade([85])

if __name__ == "__main__":
    unittest.main()
