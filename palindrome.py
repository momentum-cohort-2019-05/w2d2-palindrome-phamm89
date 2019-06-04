# User enters string
palindrometest = str(input("Enter a word, phrase, sentence, or multiple sentences: "))

# Letters of the alphabet
all_letters = "abcdefghijklmnopqrstuvwxyz"

# Blank Array
input_letters = []

# Search user's string input and enter all letters into new array
for letter in palindrometest.lower():
    if letter in all_letters:
        input_letters.append(letter)
print(input_letters)

#Compare the string forwards with the string backwards to determine if palindrome
if input_letters[:] == input_letters[::-1]:
    print("The input " + str(palindrometest) + " is a palindrome.")
else:
    print("The input " + str(palindrometest) + " is not a palindrome.")
