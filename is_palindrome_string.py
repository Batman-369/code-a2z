def is_palindrome_string(s):
    return s == s[::-1]

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

choice = input("Check Palindrome for (string/number)? ")
if choice == "string":
    s = input("Enter string: ")
    print("Palindrome" if is_palindrome_string(s) else "Not Palindrome")
elif choice == "number":
    n = int(input("Enter number: "))
    print("Palindrome" if is_palindrome_number(n) else "Not Palindrome")
