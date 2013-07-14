import copy
import collections
import operator

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


class Card(object):
    def __init__(self,val):
        self.suit = val[1]
        s = val[0]
        if s == 'T':
            self.value = 10
        elif s == 'J':
            self.value = 11
        elif s == 'Q':
            self.value = 12
        elif s == 'K':
            self.value = 13
        elif s == 'A':
            self.value = 14
        else:
            self.value = int(s)
         
    def get_card(self):
        if self.value == 10:
            val = 'T'
        elif self.value == 11:
            val = 'J'
        elif self.value == 12:
            val = 'Q'
        elif self.value == 13:
            val = 'K'
        elif self.value == 14:
            val = 'A'
        else:
            val = str(self.value)
        val += self.suit
        return val



def read_file(file_path):
    hands = []
    with open(file_path) as fp:
        hand = fp.readline().strip('\n')
        while hand:
            hand = hand.split(" ")
            cards = []
            for val in hand:
                cards.append(Card(val))
            hands.append(cards)
            hand = fp.readline().strip('\n')

    return hands



class Hand(object):
    def __init__(self,cards):
        self.cards = cards
        self.values = []
        self.suits = []
        for c in cards:
            self.values.append(c.value)
            self.suits.append(c.suit) 
        self.values.sort(reverse=True)
        self.sorted_vals = self.get_sorted_values()
        (self.singles,self.doubles,self.triples,self.fours) = self.get_sorted_lists()
        self.rank = self.categorize()


    def get_sorted_lists(self):
        singles = []
        doubles = []
        triples = []
        fours = []
        for s in self.sorted_vals:
            if s[1] == 1:
                singles.append(s[0])
            if s[1] == 2:
                doubles.append(s[0])
            if s[1] == 3:
                triples.append(s[0])
            if s[1] == 4:
                fours.append(s[0])
        singles.sort(reverse = True)
        doubles.sort(reverse = True)
        return (singles,doubles,triples,fours)


    def get_sorted_values(self):
        # returns list of tuples [(val,count)]
        x = dict(collections.Counter(self.values))
        sorted_vals = sorted(x.iteritems(), key=operator.itemgetter(1),reverse=True)
        return sorted_vals
            
    def _is_straight(self):
        if len(set(self.singles)) == 5:
            if self.singles == 14 and self.singles[1] == 4:
                    return 1
            if self.singles[0] - self.singles[4] == 4:
                return 1
        return 0
        

    def categorize(self):
        suits = []
        vals = []
        for card in self.cards:
            suits.append(card.suit)
            vals.append(card.value)
            vals.sort()
        is_straight = self._is_straight()
        is_flush = (len(set(self.suits)) == 1) 

        if is_flush:
            if is_straight:
                if self.values[0] == 14:
                    return 9
                else:
                    return 8
         
        if self.fours:
            return 7
        if self.triples:
            if self.doubles:
                return 6
        if is_flush == 1:
            return 5
        if is_straight:
            return 4
        if self.triples:
            return 3
        if len(self.doubles) == 2:
                return 2
        if self.doubles:
                return 1
        return 0

# Ranks:
# 0: High Card
# 1: One Pair
# 2: Two Pairs
# 3: Three of a Kind
# 4: Straight
# 5: Flush
# 6: Full House
# 7: Four of a Kind
# 8: Straight Flush
# 9: Royal Flush            




def play_hand(game):

    def get_high_card_winner():
       for i in range(0,5):
           if A.values[i] > B.values[i]:
               return 0
           if B.values[i] > A.values[i]:
               return 1
       print "Tie on high card"
       return 2 
        
    A = Hand(game[:5])
    B = Hand(game[5:])
    if A.rank > B.rank:
        return 0
    if B.rank > A.rank:
        return 1
    # same rank
    rank = A.rank

    if rank == 1:
        if A.doubles[0] > B.doubles[0]:
            return 0
        if B.doubles[0] > A.doubles[0]:
            return 1

    elif rank == 2:
        if A.doubles[0] > B.doubles[0]:
            return 0
        if B.doubles[0] > A.doubles[0]:
            return 1
        if A.doubles[1] > B.doubles[1]:
            return 0
        if B.doubles[1] > A.doubles[1]:
            return 1

    elif rank == 3:
        if A.triples[0] > B.triples[0]:
            return 0
        if B.triples[0] > A.triples[0]:
            return 1
    elif rank == 6:
        if A.triples[0] > B.triples[0]:
            return 0
        if B.triples[0] > A.triples[0]:
            return 1
        if A.doubles[0] > B.doubles[0]:
            return 0
        if B.doubles[0] > A.doubles[0]:
            return 1
    elif rank == 7:
        if A.fours[0] > B.fours[0]:
            return 0
        if B.fours[0] > A.fours[0]:
            return 1
 

    return get_high_card_winner()
        
            


def solve():
    # 1000 hands
    games = read_file('poker.txt')
    player_one_wins = 0
    for game in games:
        X = []
        for card in game:
            X.append(card.get_card())     
        result = play_hand(game)
        if result == 0:
            player_one_wins += 1
    return player_one_wins


if __name__== "__main__":
    ans = solve()
    print "^^^^^^^^^^^^^^^^^^"
    print ans
   
