def print_upper_words(list):
    '''Accepts a list, and returns it all capitalized. '''
    for word in list:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

print_upper_words(["eggs", "hey", "goodbye", "yo", "yes", "Eeeeeeeh"])


def print_e_words(list):
    '''Accepts a list, and returns only words that start with the letter 'e'. '''
    for word in list:
        if word.startswith("e"):
            print(word)

print_e_words(["eggs", "hey", "goodbye", "yo", "yes", "Eeeeeeeh"])

def print_msw(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


print_msw(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
