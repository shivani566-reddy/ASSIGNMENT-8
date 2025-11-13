import unittest

def is_sentence_palindrome(sentence: str) -> bool:

    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]


class TestIsSentencePalindrome(unittest.TestCase):
    
    
    # ============ Classic Palindromes ============
    def test_classic_panama(self):
        
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
    
    def test_classic_race_car(self):
        
        self.assertFalse(is_sentence_palindrome("race a car"))
    
    def test_classic_was_it_car(self):
        
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
    
    # ============ Simple Single Word Palindromes ============
    def test_single_word_palindrome(self):
        
        self.assertTrue(is_sentence_palindrome("racecar"))
    
    def test_single_word_madam(self):
        
        self.assertTrue(is_sentence_palindrome("madam"))
    
    def test_single_word_non_palindrome(self):
        
        self.assertFalse(is_sentence_palindrome("hello"))
    
    # ============ Case Sensitivity Tests ============
    def test_uppercase_palindrome(self):
        
        self.assertTrue(is_sentence_palindrome("RACECAR"))
    
    def test_mixed_case_palindrome(self):
        
        self.assertTrue(is_sentence_palindrome("RaCeCaR"))
    
    def test_lowercase_palindrome(self):
        
        self.assertTrue(is_sentence_palindrome("racecar"))
    
    def test_mixed_case_sentence(self):
        
        self.assertTrue(is_sentence_palindrome("A MaN a PlAn A CaNaL pAnAmA"))
    
    # ============ Spaces Handling ============
    def test_palindrome_with_single_space(self):
        
        self.assertTrue(is_sentence_palindrome("a b a"))
    
    def test_palindrome_multiple_spaces(self):
    
        self.assertTrue(is_sentence_palindrome("a  man  a"))
    
    def test_palindrome_leading_spaces(self):
        """Test palindrome with leading spaces"""
        self.assertTrue(is_sentence_palindrome("  racecar  "))
    
    def test_palindrome_mixed_spaces(self):
        """Test palindrome with irregular spacing"""
        self.assertTrue(is_sentence_palindrome("a   b   a"))
    
    # ============ Punctuation Handling ============
    def test_palindrome_with_period(self):
        """Test palindrome with period"""
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama."))
    
    def test_palindrome_with_question_mark(self):
        """Test palindrome with question mark"""
        self.assertTrue(is_sentence_palindrome("Madam?"))
    
    def test_palindrome_with_exclamation(self):
        """Test palindrome with exclamation mark"""
        self.assertTrue(is_sentence_palindrome("Madam!"))
    
    def test_palindrome_with_hyphens(self):
        """Test palindrome with hyphens"""
        self.assertTrue(is_sentence_palindrome("a-b-a"))
    
    def test_palindrome_with_commas(self):
        """Test palindrome with commas"""
        self.assertTrue(is_sentence_palindrome("a, b, a"))
    
    def test_palindrome_with_apostrophe(self):
        """Test palindrome with apostrophe"""
        self.assertTrue(is_sentence_palindrome("a's a"))
    
    def test_palindrome_mixed_punctuation(self):
        """Test palindrome with mixed punctuation"""
        self.assertTrue(is_sentence_palindrome("A-man, a plan; a canal: Panama!"))
    
    # ============ Numbers Handling ============
    def test_palindrome_with_numbers(self):
        """Test numeric palindrome"""
        self.assertTrue(is_sentence_palindrome("12321"))
    
    def test_palindrome_mixed_alphanumeric(self):
        """Test mixed alphanumeric palindrome"""
        self.assertTrue(is_sentence_palindrome("a1b1a"))
    
    def test_palindrome_numbers_with_spaces(self):
        """Test numeric palindrome with spaces"""
        self.assertTrue(is_sentence_palindrome("1 2 3 2 1"))
    
    def test_non_palindrome_numbers(self):
        """Test non-palindrome numbers"""
        self.assertFalse(is_sentence_palindrome("12345"))
    
    def test_palindrome_zero(self):
        """Test palindrome with zero"""
        self.assertTrue(is_sentence_palindrome("0"))
    
    # ============ Empty and Single Character ============
    def test_empty_string(self):
        """Test empty string (should be palindrome)"""
        self.assertTrue(is_sentence_palindrome(""))
    
    def test_single_character(self):
        """Test single character"""
        self.assertTrue(is_sentence_palindrome("a"))
    
    def test_single_character_uppercase(self):
        """Test single uppercase character"""
        self.assertTrue(is_sentence_palindrome("A"))
    
    def test_single_number(self):
        """Test single number"""
        self.assertTrue(is_sentence_palindrome("5"))
    
    # ============ Two Character Palindromes ============
    def test_two_char_palindrome(self):
        """Test two character palindrome"""
        self.assertTrue(is_sentence_palindrome("aa"))
    
    def test_two_char_palindrome_mixed_case(self):
        """Test two character palindrome with mixed case"""
        self.assertTrue(is_sentence_palindrome("Aa"))
    
    def test_two_char_non_palindrome(self):
        """Test two character non-palindrome"""
        self.assertFalse(is_sentence_palindrome("ab"))
    
    # ============ Complex Sentences ============
    def test_complex_palindrome_able(self):
        """Test Able was I ere I saw Elba"""
        self.assertTrue(is_sentence_palindrome("Able was I ere I saw Elba"))
    
    def test_complex_palindrome_never_odd(self):
        """Test Never odd or even"""
        self.assertTrue(is_sentence_palindrome("Never odd or even"))
    
    def test_complex_palindrome_geese(self):
        """Test Do geese see God"""
        self.assertTrue(is_sentence_palindrome("Do geese see God?"))
    
    def test_complex_palindrome_taco(self):
        """Test Was it a rat I saw"""
        self.assertTrue(is_sentence_palindrome("Was it a rat I saw?"))
    
    def test_complex_non_palindrome(self):
        """Test non-palindrome sentence"""
        self.assertFalse(is_sentence_palindrome("Hello World"))
    
    def test_complex_palindrome_poor(self):
        """Test A poor man poor"""
        self.assertFalse(is_sentence_palindrome("A poor man"))
    
    # ============ Whitespace Only and Punctuation Only ============
    def test_spaces_only(self):
        """Test spaces only (should be palindrome)"""
        self.assertTrue(is_sentence_palindrome("   "))
    
    def test_punctuation_only(self):
        """Test punctuation only (should be palindrome)"""
        self.assertTrue(is_sentence_palindrome("!!!???..."))
    
    def test_mixed_whitespace_punctuation(self):
        """Test mixed whitespace and punctuation"""
        self.assertTrue(is_sentence_palindrome("  , . ! ? ; :  "))
    
    # ============ Special Characters ============
    def test_palindrome_with_special_chars(self):
        """Test palindrome with special characters"""
        self.assertTrue(is_sentence_palindrome("A1@B@1A"))
    
    def test_palindrome_with_brackets(self):
        """Test palindrome with brackets"""
        self.assertTrue(is_sentence_palindrome("[a b a]"))
    
    def test_palindrome_with_underscore(self):
        """Test palindrome with underscore"""
        self.assertTrue(is_sentence_palindrome("a_b_a"))
    
    # ============ Invalid Inputs ============
    def test_none_input_raises(self):
        """Test None input raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(None)
    
    def test_integer_input_raises(self):
        """Test integer input raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(12321)
    
    def test_float_input_raises(self):
        """Test float input raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(123.21)
    
    def test_list_input_raises(self):
        """Test list input raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(["a", "b", "a"])
    
    def test_dict_input_raises(self):
        """Test dict input raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome({"key": "value"})


class TestCaseSummary(unittest.TestCase):
    """Summary and documentation of all test cases"""
    
    def test_print_summary(self):
        """Print comprehensive test summary"""
        print("\n" + "="*80)
        print("COMPREHENSIVE TEST CASE SUMMARY FOR is_sentence_palindrome()")
        print("="*80)
        print("\n📋 TEST CATEGORIES (40+ Test Cases):\n")
        
        categories = {
            "1. Classic Palindromes": [
                "✓ A man a plan a canal Panama",
                "✗ race a car",
                "✓ Was it a car or a cat I saw?"
            ],
            "2. Simple Single Words": [
                "✓ racecar, madam",
                "✗ hello, world"
            ],
            "3. Case Sensitivity": [
                "✓ RACECAR, RaCeCaR, racecar",
                "✓ Mixed case sentences preserved"
            ],
            "4. Spaces Handling": [
                "✓ Single and multiple spaces",
                "✓ Leading/trailing spaces",
                "✓ Irregular spacing"
            ],
            "5. Punctuation Handling": [
                "✓ Periods, commas, question marks",
                "✓ Exclamation marks, hyphens, apostrophes",
                "✓ Mixed punctuation"
            ],
            "6. Numbers Handling": [
                "✓ 12321, a1b1a",
                "✗ 12345",
                "✓ Numeric palindromes with spaces"
            ],
            "7. Edge Cases": [
                "✓ Empty string (palindrome)",
                "✓ Single character (palindrome)",
                "✓ Two character palindromes/non-palindromes"
            ],
            "8. Complex Sentences": [
                "✓ Able was I ere I saw Elba",
                "✓ Never odd or even",
                "✓ Do geese see God?"
            ],
            "9. Special Cases": [
                "✓ Spaces only, punctuation only",
                "✓ Special characters (@, [], _)",
                "✓ Mixed whitespace and punctuation"
            ],
            "10. Invalid Inputs": [
                "✗ None (TypeError)",
                "✗ Integer (TypeError)",
                "✗ Float, List, Dict (TypeError)"
            ]
        }
        
        for category, tests in categories.items():
            print(f"{category}")
            for test in tests:
                print(f"   {test}")
            print()
        
        print("="*80)
        print("✅ TOTAL: 40+ Comprehensive Test Cases")
        print("="*80 + "\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)