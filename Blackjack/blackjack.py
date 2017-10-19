# Card Class, Deck Class, Hand Class
from random import shuffle
import random


# Blackjack
ranks = ('A','2','3','4','5','6','7','8','9','T','J','Q','K')
suits = ('C','D','H','S')

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck(object):
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def __str__(self):
        cards_in_deck = ''
        for card in self.cards:
            cards_in_deck = cards_in_deck + str(card) + ' '
        return cards_in_deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop(0)
        return card

    def shuffle(self):
        for i in range(len(deck) - 1, 0, -1):
            j = random.randrange(i + 1)
            deck[i], deck[j] = deck[j], deck[i]



# class Hand(object):
#     def __init__(self):
#         self.hand = []
#
#     def add_card(self, card):
#         self.hand.append(card)
#         return self.hand
#
#     def get_value(self):
#         def get_value(self):
#             value = sum(card.point for card in self.cards)
#             aces = sum(card.is_ace for card in self.cards)
#             while (value > 21) and aces:
#                 value -= 10
#                 aces -= 1
#                 return value
#
# if __name__ == '__main__':
#     deck =
card1 = Deck()
print(card1.deal_card)
