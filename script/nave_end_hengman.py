from random import randint
from collections import Counter

HANGMAN_PHOTOS = {1: "    x-------x", 2:
    """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |
""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 5: """    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
""", 6: """    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
""", 7: """    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |"""}


def welcome_screen():
    """
    print welcome screen
    :return: welcome screen
    :rtype: str
    """
    print("""   _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/
    """)
    print(randint(5, 10))


def show_hidden_word(secret_word, old_letters_guessed):
    """
    collected string of secret word and collect
    list of letters hes guessed and return
    string of some correct guessed
    :param secret_word: string of secret word
    :type secret_word: str
    :param old_letters_guessed: list of letters hes guessed
    :type old_letters_guessed: list
    :return: string of some correct guessed
    :rtype:str
    """
    # old_letters_guessed = old_letters_guessed.split(" -> ")
    len_secret_word = len(secret_word)
    lst1 = len_secret_word * ["_"]
    for char in old_letters_guessed:
        for place in range(len(secret_word)):
            if char == secret_word[place]:
                lst1[place] = char
    lst1 = " ".join(lst1)
    return lst1


def print_hangman(num_of_tries):
    """
    collected a number between 1 - 7 and return status of the number he was lose in the hangman.
    :param num_of_tries: number between 1 - 7
    :type num_of_tries: int
    :return: status of the number he was lose in the hangman
    :rtype: str
    """
    print(HANGMAN_PHOTOS[num_of_tries])




def check_valid_input(letter_guessed, old_letters_guessed):
    """
    collected leter and check if the
    letter proper
    :param letter_guessed: guess letter
    :type letter_guessed: str
    :param old_letters_guessed:
    :type old_letter_guessed: list
    :return: if letter proper return true and update
    old_letters_guessed if letter not proper return false
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    len_letter = len(letter_guessed)
    if int(len_letter) > 1:
        return False
    elif not (letter_guessed.isalpha()):
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    collected leter and check if the
    letter proper return true and update
    old_letters_guessed if letter not proper return false
    :param letter_guessed: guess letter
    :type letter_guessed: str
    :param old_letters_guessed:
    :type old_letter_guessed: list
    :return: collected leter and check if the
    letter proper return true and update
    old_letters_guessed if letter not proper return false
    :rtype: bool
    """
    old_letters_guessed = sorted(old_letters_guessed)
    letter_guessed = letter_guessed.lower()
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        print(" -> ".join(old_letters_guessed))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def check_win(secret_word, old_letters_guessed):
    """
    collected string of secret word and collect
    list of letters hes guessed and return
    true if in old_letters_guessed has the letters his
    in secret_word false if not
    :param secret_word: string of secret word
    :type secret_word: str
    :param old_letters_guessed: list of letters hes guessed
    :type old_letters_guessed: list
    :return: true if in old_letters_guessed has the letters his
    in secret_word false if not
    :rtype:bool
    """
    len_secret_word = len(secret_word)
    lst1 = len_secret_word * [""]

    for char in old_letters_guessed:
        for place in range(len(secret_word)):
            if char == secret_word[place]:
                lst1[place] = char
    lst1 = "".join(lst1)
    return secret_word == lst1

def guess_a_letter():
    """
    collected a letter form the player
    :return: the letter form the player
    :rtype: str
    """
    letter_guessed = input("plese Guess a letter: ")
    return letter_guessed


def in_word(hidden_word, letter):
    """
    check if letter Guess is in secret word
    :param hidden_word: the secret word
    :type: str
    :param letter: letter Guess
    :type: str
    :return: True or False
    :rtype: bool
    """
    return letter in hidden_word


def choose_word(file_path, index):
    """
    the function return tuple of The number of different words in the file
    that is, does not include repetitive words and word in index was the function was collected
    :param file_path: path to txt file
    :type: str
    :param index: index in a word in txt file
    :type: int
    :return:tuple of The number of different words in the file
    that is, does not include repetitive words and word in index was the function was collected
    :rtype: int and str
    """

    with open(file_path, "r") as file:
        redeing = file.read()
        redeing = redeing.split(" ")

        for i in range(0, len(redeing)):
            redeing[i] = "".join(redeing[i])
        file = Counter(redeing)
        none_duplicates_list = " ".join(file.keys())
        none_duplicates_list.split(" ")
        len_redeing = len(redeing)
        if index >= len_redeing:
            index = index % len_redeing
        end_word = redeing[index-1]
        return end_word

def main():
    """
    this func wos doing the hangman was played
    :return: the hangman game
    :rtype: str
    """
    welcome_screen()
    # The file path: c:\Users\Admin\Desktop\python_file_text\words.txt
    print("Let’s start!!!!\n")
    the_word = choose_word(input("Enter file path: "), int(input("Enter index: ")))
    num_of_tries = 1

    old_letters_guessed = []
    print_hangman(num_of_tries)
    print(show_hidden_word(the_word, old_letters_guessed))
    while num_of_tries <= 7:
        letter = guess_a_letter().lower()
        update_succeeded = try_update_letter_guessed(letter, old_letters_guessed)
        if update_succeeded:
            old_letters_guessed.append(letter)
            if not in_word(the_word, letter):
                print("):")
                num_of_tries += 1
                print_hangman(num_of_tries)
            hidden_word = show_hidden_word(the_word, old_letters_guessed)
            print(hidden_word)
        won = check_win(the_word, old_letters_guessed)
        if won:
            print("WIN")
            break
        elif num_of_tries == 7 and not won:
            print("LOSE")
            break


if __name__ == '__main__':
    main()
