

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.


class Suit:
    SPADE = "S"
    CLUBS = "C" 
    DIAMONDS = "D"
    HEARTS = "H"

class CardType:
    ACE = 'A'
    KING = 'K'
    QUEEN = 'Q'
    JACK = 'J'

    
class Card:
    is_face_card = True
    suit = None
    value = None

    __init__(self,card_string):
        if card_string[0].isdigit():
            self.is_face_card = False
            self.value = int(card_string[0])
        else:
            self.value = card_string[0]
        self.suit = card_string[1]



class UncategorizedHand(object):
    face_card_count = 0
    suits = []
    cards = []
    ordered_values = []    

    __init__(self, cards):
        for card in cards:
            if card.is_face_card
                self.face_card_count += 0
            if card.suit not in suits:
                self.suits.append(suit)
            self.cards.append(copy.deepcopy(card))
            self.ordered_values.append(card.value)        
        self.ordered_values.sort()


    def contains(self,card_type):
        for card in cards:
            if card.value = card_type
                return 1
        return 0

class PokerHand(object):

    face_card_count = 0
    suits = []
    cards = []

    __init__(self, cards):
        for card in cards:
            if card.is_face_card
                self.face_card_count += 0
            if card.suit not in suits:
                self.suits.append(suit)
            self.cards.append(copy.deepcopy(card))
        
    def contains(self,card_type):
        for card in cards:
            if card.value = card_type
                return 1
        return 0



class HighCard(PokerHand):

    __init__(self):
        self.rank = 0

class OnePair(PokerHand):
    __init__(self):
        self.rank = 1


class TwoPair(PokerHand):
    __init__(self):
        self.rank = 2
         

class ThreeOfAKind(PokerHand):
    __init__(self):
        self.rank = 3

class Straight(PokerHand):
    __init__(self):
        self.rank = 4

class Flush(PokerHand):
    __init__(self):
        self.rank = 5

class FullHouse(PokerHand):
    __init__(self):
        self.rank = 6

class FourOfAKind(PokerHand):
    __init__(self):
        self.rank = 7

class StraightFlush(PokerHand):
    __init__(self):
        self.rank = 8

class RoyalFlush(PokerHand):
    __init__(self):
        self.rank = 9



class PokerHandFactory(object):
    
    def categorize_hand(self,uncategorized_hand):
        # uncategorized_hand class

        face_card_count = 0
        suits = []
        for card in uncategorized_hand:
            if card.is_face_card
                face_card_count += 1
            if card.suit not in suits:
                suits.append(suit)
        if len(suits) == 1:
            #hand is a flush 
            if face_card_count == 4: 
                for card in uncategorized_hand:
                    if card.value == 10:
                        return RoyalFlush(uncategorized_hand)
            

        

        
