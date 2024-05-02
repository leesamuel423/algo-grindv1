def is_palindrome(x):
    # A negative number cannot be a palindrome
    if x < 0:
        return False

    # Store the original number to compare later
    original = x
    reversed_number = 0

    while x > 0:
        # Extract the last digit of the number
        digit = x % 10
        # Add the digit to the reversed number
        reversed_number = reversed_number * 10 + digit
        # Remove the last digit from the original number
        x //= 10

    # Check if the reversed number is equal to the original number
    return original == reversed_number

# Test cases
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(0))   # Output: False
