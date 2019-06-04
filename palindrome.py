palindrometest = str(input("Enter a word, phrase, sentence, or multiple sentences: "))

all_letters = "abcdefghijklmnopqrstuvwxyz"
input_letters = []

for letter in palindrometest.lower():
    if letter in all_letters:
        input_letters.append(letter)
    # print(input_letters)

if input_letters[:] == input_letters[::-1]:
    print("The input " + str(palindrometest) + " is a palindrome.")
else:
    print("The input " + str(palindrometest) + " is not a palindrome.")
