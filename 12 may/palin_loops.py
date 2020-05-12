def reverse(word):
    reverse_word = ''
    for i in range(len(word)):
        reverse_word += word[len(word)-1-i]
    return reverse_word

word = input("Type in a word:\n")
x = reverse(word)
if x == word:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
