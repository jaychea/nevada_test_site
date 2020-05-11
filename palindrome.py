word = input("Type in a word: ")
print("You've typed in " + word + ".")

word = str(word)
reverse_word = word[::-1]
print(reverse_word.lower())


if word == reverse_word:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")