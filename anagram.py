given = list(input('Please enter the first word you would like to use.: '))
test = list(input('Please enter the word you would like to test.: '))
def determine(given, test):
    if len(given) == len(test):
        return True
    elif len(given) != len(test):
        return False
def anagram(given, test):
    given = sorted(given)
    test = sorted(test)
    if given == test:
       print("This is an anagram.")
    else:
        print("This is not an anagram.")
anagram(given, test)
