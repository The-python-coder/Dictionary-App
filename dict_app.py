from PyDictionary import PyDictionary
from difflib import get_close_matches
from english_words import english_words_alpha_set


word_list = list(english_words_alpha_set)
dict = PyDictionary()


def do_you_want_to_use_me():
    while True:
        yn = input("Do you want to use me? Y for yes, N for no").upper()
        if yn == "Y":
            return True
        elif yn == "N":
            return False
        else:
            print("Sorry, did not understand your response! Try again.")
            continue


def do_you_want_to_use_me_again():
    while True:
        yn = input("Do you want to use me again?? Y for yes, N for no").upper()
        if yn == "Y":
            return True
        elif yn == "N":
            return False
        else:
            print("Sorry, did not understand your response! Try again.")
            continue


def dictionary():
    f = open("meanings.txt", "a")
    try:
        word = input("Type a word to get its meaning and hit enter: ")
        meaning = dict.meaning(word)
        i = 0
        f.write(word + ": \n")
        for type, definition in meaning.items():
            f.write(type + ": \n")
            for m in definition:
                i += 1
                f.write(f"{i}.{m}\n")
        f.write("\n")
        f.write("\n")
    except:
        print("Sorry, the word does not exist! Please re-check!")


def main():
    while True:
        if do_you_want_to_use_me():
            dictionary()
            if do_you_want_to_use_me_again():
                dictionary()
            else:
                print("Have a great day!")
                break
        else:
            print("Have a great day!")
            break


if __name__ == "__main__":
    main()