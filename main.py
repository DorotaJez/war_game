import random

class Deck:
    # a list of 52 cards
    # shuffle
    # split (into two PlayerCards instances)
    pass

class PlayerCards:
    # a list of 26 cards, inherits that attribute from Deck
    # but doesn't have to inherit shuffle and split methods
    # withdraw - 1 card from the top
    # add_cards - x cards to the bottom
    # check_if_empty? or just len
    pass

class Table:

    order_dict = dict(zip(["2","3","4","5","6","7","8","9","10","J","Q","K","A"], range(2,15)))

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

def normal_game(table,p1,p2):
    while True:
        if len(p1.cards) <= 0 or len(p2.cards) <= 0:
            break
        # do you want to exit? message
        # if not
        # enter
        card_a = p1.withdraw()
        card_b = p2.withdraw()
        table.add_to_table(card_a, card_b)
        print(table)
        if table.compare() == "card a":
            p1.add_cards(table)
        elif table.compare() == "card b":
            p2.add_cards(table)
        else:
            war_scenario()
    pass

def war_scenario():
    pass

if __name__ == "__main__":
    main()
