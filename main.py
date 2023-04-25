import random
import sys

class Deck:
    '''represents an entire 52-cards deck'''
    global card_ranks
    card_ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    card_suits = ["♠", "♥", "♦", "♣"]

    def __init__(self, card_suits=card_suits, card_ranks=card_ranks):
        self.cards = [rank+suit for rank in card_ranks for suit in card_suits]

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards  
    
    def split(self):
        p1 = PlayerCards(self.cards[:26])
        p2 = PlayerCards(self.cards[26:])
        return p1, p2
    

class PlayerCards:
    '''all of the cards for an individual user'''
    def __init__(self, cards):
        self.cards = cards

    def withdraw(self):
        self.cards = self.cards[1:]
        return self.cards[0]

    def add_cards(self, cards_to_add):
        self.cards += cards_to_add
    

class Table:
    '''represents the playing table, contains the cards that are currently on the table and is able to compare their ranks'''
    order_dict = dict(zip(card_ranks, range(2,15)))

    def __init__(self, current_state={"P1": [], "P2": []}):
        self.current_state = current_state

    def __str__(self):
        return f"Player 1: {self.current_state['P1']}, Player 2: {self.current_state['P2']}"

    def add_to_table(self, card_a, card_b):
        self.current_state['P1'] = [card_a] + self.current_state['P1']
        self.current_state['P2'] = [card_b] + self.current_state['P2']

    def compare(self):
        card_a = self.current_state['P1'][0]
        card_b = self.current_state['P2'][0]
        if self.order_dict[card_a[:-1]] > self.order_dict[card_b[:-1]]:
            return "card a"
        elif self.order_dict[card_a[:-1]] < self.order_dict[card_b[:-1]]:
            return "card b"
        else:
            return "tie"

    def clear(self):
        self.current_state['P1'] = []
        self.current_state['P2'] = []


class Game:    
    def normal_game(self, table,p1,p2):
        while True:
            if len(p1.cards) <= 0:
                self.end_game("Player 2")
            if len(p2.cards) <= 0:
                self.end_game("Player 1")
            if input() == "exit":
                self.end_game()
            card_a = p1.withdraw()
            card_b = p2.withdraw()
            table.add_to_table(card_a, card_b)
            print(table)
            if table.compare() == "card a":
                p1.add_cards(table.current_state["P1"] + table.current_state["P2"])
                print(f"Player 1 has won this round. They now have {len(p1.cards)} cards")
            elif table.compare() == "card b":
                p2.add_cards(table.current_state["P1"] + table.current_state["P2"])
                print(f"Player 2 has won this round. They now have {len(p1.cards)} cards")
            else:
                self.war_scenario(table,p1,p2)
            table.clear()


    def war_scenario(self,table,p1,p2):
        while True:
            if len(p1.cards) <= 0:
                self.end_game("Player 2")
            if len(p2.cards) <= 0:
                self.end_game("Player 1")
            if input() == "exit":
                self.end_game()  

            print("Press enter to put a card facing down...")

            if input() != None:
                card_a_face_down = p1.withdraw()
                card_b_face_down = p2.withdraw()
                table.add_to_table(card_a_face_down, card_b_face_down) 

            user_input = input("Press enter again to put a card facing up...")

            if user_input != None:
                card_a_face_up = p1.withdraw()
                card_b_face_up = p2.withdraw()
                table.add_to_table(card_a_face_up, card_b_face_up)
                print(table)

                if table.compare() == "card a":
                    p1.add_cards(table.current_state["P1"] + table.current_state["P2"])
                    print("Player 1 has won the war!")
                    return
                elif table.compare() == "card b":
                    p2.add_cards(table.current_state["P1"] + table.current_state["P2"])
                    print("Player 2 has won the war!")
                    return
                else:
                    print("The war goes on!")
                    self.war_scenario(table,p1,p2)    
                          

    def end_game(self, winner=None):
        if winner != None:
            print(f"{winner} has won the game!")
        sys.exit("Thanks for playing!")

def main():
    print("Welcome to the War Game! Press enter to begin")
    game = Game()
    deck = Deck()
    table = Table()
    deck.shuffle()
    p1, p2 = deck.split()
    game.normal_game(table,p1,p2)

if __name__ == "__main__":
    main()
