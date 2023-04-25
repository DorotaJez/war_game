import random
import sys

class Deck:
    '''represents an entire 52-cards deck'''
    global card_ranks
    card_ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    card_suits = ["♠", "♥", "♦", "♣"]

    def __init__(self, card_suits=card_suits, card_ranks=card_ranks):
        self.cards = [rank+" "+suit for rank in card_ranks for suit in card_suits]

    def shuffle(self):
        return random.shuffle(self.cards)  
    
    def split(self):
        p1 = PlayerCards(self.cards[:26])
        p2 = PlayerCards(self.cards[26:])
        return p1, p2
    

class PlayerCards:
    '''all of the cards for an individual user'''
    # no inheritance - add that to readme etc.
    def __init__(self, cards):
        self.cards = cards

    def withdraw(self):
        return self.cards[0]

    def add_cards(self, cards_to_add):
        self.cards.append(cards_to_add)
    

class Table:
    '''represents the playing table, contains the cards that are currently on the table and is able to compare their ranks'''
    order_dict = dict(zip(card_ranks, range(2,15)))

    def __init__(self, current_state={"P1": [], "P2": []}):
        self.current_state = current_state
        self.player_one_cards = current_state["P1"]
        self.player_two_cards = current_state["P2"]
        self.all_cards = self.player_one_cards + self.player_two_cards

    def __str__(self):
        return f"Player 1: {self.player_one_cards}, Player 2: {self.player_two_cards}"

    def add_to_table(self, card_a, card_b):
        self.player_one_cards.append(card_a)
        self.player_two_cards.append(card_b)

    def compare(self):
        card_a = self.player_one_cards[0]
        card_b = self.player_two_cards[0]
        if self.order_dict[card_a[:-1]] > self.order_dict[card_b[:-1]]:
            return "card a"
        elif self.order_dict[card_a[:-1]] < self.order_dict[card_b[:-1]]:
            return "card b"
        else:
            return "tie"        

    def clear(self):
        self.current_state = {"P1": [], "P2": []}

def main():
    deck = Deck()
    table = Table()
    deck.shuffle()
    p1, p2 = deck.split()
    normal_game(table,p1,p2)

def normal_game(table,p1,p2): # create a separate class for normal_game, war_scenario and end_game?
    while True:
        if len(p1.cards) <= 0:
            end_game(p2)
        if len(p2.cards) <= 0:
            end_game(p1)
        if input() == "exit": # the player can type anything else and continue playing - iclude that in the description
            end_game()
        card_a = p1.withdraw()
        card_b = p2.withdraw()
        table.add_to_table(card_a, card_b)
        print(table)
        if table.compare() == "card a":
            p1.add_cards(table.all_cards)
        elif table.compare() == "card b":
            p2.add_cards(table.all_cards)
        else:
            war_scenario(table,p1,p2)

def war_scenario():
    pass

def end_game(winner=None):
    if winner != None:
        print(f"{winner} has won the game!")
    sys.exit("Thanks for playing!")

if __name__ == "__main__":
    main()
