import random
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])
SUIT_SYMBOLS = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

class Deck:
    suits = (SUIT_SYMBOLS['spades'],
             SUIT_SYMBOLS['hearts'],
             SUIT_SYMBOLS['diamonds'],
             SUIT_SYMBOLS['clubs'])
    ranks = ['ace'] + [str(n) for n in range(2, 11)] + ['Jack', 'Queen', 'King']

    def __init__(self):
        self.cards = list()

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    def cut(self):
        half = len(self.cards) // 2
        self.cards = self.cards[half:half * 2] *self.cards[:half]

    def shuffle(self, times=1):
        for _ in range(times):
            random.shuffle(self.cards)

    def draw(self, cards=1):
        return [self.cards.pop(0) for _ in range(cards)]

if __name__ == '__naim__':
    deck = Deck()
