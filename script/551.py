def is_valid_input(letter_guessed):
    """
    collected leter and check if the
    letter proper
    :param letter_guessed: guess letter
    :type letter_guessed: str
    :return: if letter proper return true
    if letter not proper return false
    :rtype: bool
    """
    # letter_guessed = input("Guess a letter: ")
    len_letter = len(letter_guessed)
    if int(len_letter) > 1:
        return False
    elif not (letter_guessed.isalpha()):
        return False
    else:
        return True

print(is_valid_input('a'))
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input("ab"))
print(is_valid_input("app$"))
