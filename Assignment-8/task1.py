def is_valid_email(email: str) -> bool:
    """
    Validate email address based on specific requirements:
    - Must contain @ and . characters
    - Must not start or end with special characters
    - Should not allow multiple @ symbols
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if email is valid, False otherwise
    """
    # Check if email is empty or not a string
    if not email or not isinstance(email, str):
        return False
    
    email = email.strip()
    
    # Check if email contains exactly one @ symbol
    if email.count('@') != 1:
        return False
    
    # Check if email contains at least one . (dot)
    if '.' not in email:
        return False
    
    # Split email into local and domain parts
    local, domain = email.split('@')
    
    # Check if local or domain part is empty
    if not local or not domain:
        return False
    
    # Check if local part starts or ends with special characters
    if local[0] in '.-_' or local[-1] in '.-_':
        return False
    
    # Check if domain part starts or ends with special characters
    if domain[0] in '.-_' or domain[-1] in '.-_':
        return False
    
    # Check if domain has at least one dot and proper structure
    if domain.count('.') < 1:
        return False
    
    # Check domain parts are not empty
    domain_parts = domain.split('.')
    for part in domain_parts:
        if not part:
            return False
    
    # Check last domain part (TLD) has at least 2 characters
    if len(domain_parts[-1]) < 2:
        return False
    
    return True


def run_test_cases():
    """Run comprehensive test cases for email validator."""
    test_cases = [
        # Valid emails
        ("john@example.com", True, "Standard valid email"),
        ("user.name@domain.co.uk", True, "Email with dot in local part"),
        ("test123@test.org", True, "Email with numbers"),
        ("a@b.co", True, "Minimal valid email"),
        
        # Invalid - Missing @ symbol
        ("johnexample.com", False, "Missing @ symbol"),
        
        # Invalid - Missing dot
        ("john@example", False, "Missing dot in domain"),
        
        # Invalid - Multiple @ symbols
        ("john@@example.com", False, "Multiple @ symbols"),
        ("john@doe@example.com", False, "Multiple @ symbols (2)"),
        
        # Invalid - Starts with special character
        (".john@example.com", False, "Starts with dot"),
        ("-john@example.com", False, "Starts with hyphen"),
        ("_john@example.com", False, "Starts with underscore"),
        
        # Invalid - Ends with special character
        ("john.@example.com", False, "Local part ends with dot"),
        ("john-@example.com", False, "Local part ends with hyphen"),
        ("john_@example.com", False, "Local part ends with underscore"),
        
        # Invalid - Domain issues
        ("john@.example.com", False, "Domain starts with dot"),
        ("john@example.com.", False, "Domain ends with dot"),
        ("john@example..com", False, "Domain has consecutive dots"),
        ("john@-example.com", False, "Domain starts with hyphen"),
        ("john@example-.com", False, "Domain ends with hyphen"),
        
        # Invalid - Empty parts
        ("@example.com", False, "Missing local part"),
        ("john@", False, "Missing domain part"),
        ("", False, "Empty string"),
        
        # Invalid - TLD too short
        ("john@example.c", False, "TLD with only 1 character"),
        
        # Invalid - Special characters
        ("john#doe@example.com", False, "Special character in local part"),
        ("john@exam ple.com", False, "Space in domain"),
    ]
    
    print("Email Validator Test Cases")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for email, expected, description in test_cases:
        result = is_valid_email(email)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"{status} | {email:30} | {description}")
        if result != expected:
            print(f"       Expected: {expected}, Got: {result}")
    
    print("=" * 70)
    print(f"Total: {len(test_cases)} | Passed: {passed} | Failed: {failed}")


def get_user_input() -> str:
    """Get email input from user with validation."""
    while True:
        email = input("Enter email address to validate: ").strip()
        if email:
            return email
        print("Please enter a non-empty email.")


def main():
    print("Email Validator Application\n")
    
    while True:
        print("\nOptions:")
        print("1. Run test cases")
        print("2. Validate custom email")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            run_test_cases()
        
        elif choice == '2':
            email = get_user_input()
            is_valid = is_valid_email(email)
            print(f"\nEmail: {email}")
            print(f"Valid: {'Yes ✓' if is_valid else 'No ✗'}")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()