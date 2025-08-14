def is_palindrome(s):
    rev=""
    for char in s:
        rev = char + rev
    return s == rev
print(is_palindrome("madam"))
print(is_palindrome("window"))
print(is_palindrome("bud"))
