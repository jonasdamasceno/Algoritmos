def is_palindrome_iterative(word):
    if word == "":
        return False

    new_word = word[::-1]

    if new_word == word:
        return True
    else:
        return False
