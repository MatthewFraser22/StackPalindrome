from function import palindrome


print("Enter a word to determine if it is a palindrome.")
pal = (input(": "))

result = palindrome(pal)

if result == True:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
