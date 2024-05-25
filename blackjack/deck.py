import random

from values import ranks, suits, values
from card import Card

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):

        single_card = self.deck.pop()
        return single_card







