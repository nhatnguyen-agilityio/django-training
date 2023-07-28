import random

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
    '8', '9', '10', 'Jack', 'Queen', 'King']
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def __lt__(self):
        sorted(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, hands, cards):
        hand_cards = {}
        for i in range(hands):
            list_cards = []
            for j in range(cards):
                suit = random.randint(0, 3)
                rank = random.randint(0, 11)
                card = Card(suit, rank)
                list_cards.append(card)
            hand_cards["hand {0}".format(i+1)] = list_cards
        return hand_cards

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

queen_of_diamonds = Card(1, 12)
deck = Deck()
cards_of_hands = deck.deal_hands(4, 12)
for hand in cards_of_hands:
    print(hand)
    for card in cards_of_hands[hand]:
        print(card)