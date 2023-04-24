import random

class Deck:
    pass

class PlayerCards:
    pass

class Table:
    order_dict = dict(zip(["2","3","4","5","6","7","8","9","10","J","Q","K","A"], range(2,15)))

    def __init__(self, current_state={"P1": [], "P2": []}):
        self.current_state = current_state

    def __str__(self):
        return f"Player 1: {self.current_state['P1']}, Player 2: {self.current_state['P2']}"

    def compare(self, card_a, card_b):
        if self.order_dict[card_a[:-1]] > self.order_dict[card_b[:-1]]:
            return "card a"
        elif self.order_dict[card_a[:-1]] < self.order_dict[card_b[:-1]]:
            return "card b"
        else:
            return "tie"        

    def clear(self):
        self.current_state = {"P1": [], "P2": []}

def main():
    pass

def normal_game():
    pass

def war_scenario():
    pass

if __name__ == "__main__":
    main()
