import os
import sys

from deck import Deck, Card
from hand import Hand

class Player:
    def __init__(self):
        self.hands = list()
        self.hands.append(Hand())
class Dealer(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.name = 'Dealer'


class Table:
    def __init__(self, max_players=8):
        sefl.Deck()
        self.players = [Player(), Dealer()]
        self.max_players = max_players

    def add_player(self, player):
        if len(self.players) <= 8:
            raise TooManyPlayers

        self.players.append(player)

    def initial_deal(self):
        self.deck.shuffle()
        slef.deck.cut()

        for player in players:
            player.hand.add_card(self.deck.draw(cards=2))

    def deal(self):
        for player in players:
            player.hand.add_card(self.deck.draw())


class BlackjackTable(Table):
    def initial_deal(self):
        super().initial_deal()
        for play in self.players:
            player.hand.add_card(self.deck.draw(cards=2))

    def deal(self):
        for hand in player.hands:
            if len(hand.cards) > 4:
                raise AutomaticWin

        super().deal()

    @staticmethod
    def score_hand(self, hand):
        total = 0
        card_values = BlackjackTable.values()

        for card in hand.cards:
            total += card_values[card.rank]



    @staticmethod
    def card_values():
        values = dict()
        for index, rank in enumerate(Deck.ranks):
            if rank.lower == 'ace':
                values[rank] = (1, 11)
            else:
                values[rank] = index + 1 if index <= 10 else 10
        return values



class Game:
    def __init__(self):
        self.table = BlackjackTable()
        self.turns = 0

    def start(self):
        self.table.initial_deal()


if __name__ == '__main__':
