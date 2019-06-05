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

#Iterative function to determine if string is palindrome
def palindrome_iteration(input_letters):
    """Compare letters in input_letters to determine if palindrome."""
    counter = 0
    endcounter = len(input_letters) - 1
    if len(input_letters) == 1 or len(input_letters) == 0:
        palindrome = "The input " + str(palindrometest) + " is a palindrome."
        return print(str(palindrome))
    elif input_letters[0] != input_letters[-1]:
        not_palindrome = "The input " + str(palindrometest) + " is not a palindrome."
        return print(str(not_palindrome))
    elif input_letters[counter] == input_letters[endcounter]:
        while counter <= len(input_letters):
            if input_letters[counter] == input_letters[endcounter]:
                counter += 1
                endcounter -= 1
                palindrome = "The input " + str(palindrometest) + " is a palindrome."
                return print(str(palindrome))
            else:
                not_palindrome = "The input " + str(palindrometest) + " is not a palindrome."
                return print(str(not_palindrome))
    else:
        return print(str(palindrome))

palindrome_iteration(input_letters)
