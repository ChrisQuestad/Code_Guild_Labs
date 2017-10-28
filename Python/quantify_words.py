
import string
from operator import itemgetter


def clean_file(st):
    """
    Cleans a text file of:
    punctuation
    new line characters
    spaces

    returns a list of strings cast to lower case.
    """
    punct = set(string.punctuation)
    new_str = ''
    for char in st:
        if char not in punct and char not in '\n':
            new_str += char.lower()
    word_lst = new_str.split(' ')
    new_word_lst = []
    for word in word_lst:
        if len(word) > 0:
            new_word_lst.append(word)
    return new_word_lst


def count_words(word_lst):
    word_count = {}
    for word in word_lst:
        try:
            word_count[word] += 1
        except KeyError:
            word_count[word] = 1
    return word_count


def find_top_n(word_dict,):
    word_tup = word_dict.items()
    top_list = sorted(word_tup, key=itemgetter(1), reverse=True)
    return top_list


def display_top(top_list):
    length = len(top_list)
    # print("the Top {} words are:".format(length))
    for t in top_list:
        print('{} {}'.format(t[0], t[1]))


def quantify_words(text):
    word_list = clean_file(text)
    display_top(find_top_n(count_words(word_list)))


if __name__ == "__main__":
    with open('AliceInWonderland.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
    quantify_words(text)
