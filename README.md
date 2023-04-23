# War Game
##### A Turing College Pair Programming Project

### Description
This project's aim is to practice OOP principles as well as version control and pair programming by the means of creating a simple card game called "war".

### Requirements and Setup
There are no special requirements to play this game other than a Python interpreter and a functioning keyboard.
In order to setup the program, simply run the "main.py" script.   

### The Rules
The rules of the game are quite simple. You're going to play against a computer, but since it's a totally randomized game that doesn't rely much on the player's decision, you could also assume that the computer's "choices" are  actually somebody else's, for example, of a person who is willing to play with you.
For the sake of simplicity, we will call the two players P1 (user) and P2 (computer).
The goal of the game is to take posession of all the cards of the opponent.
The steps of the game are as follows:
1. At the beginning the deck is randomly and equally split between P1 and P2.
2. P1 presses "enter" to play the first card from their deck (which is a queue structure).
3. At the same time, P2 also pulls out the first card.
4. Both cards appear on the screen and are compared (just by their value: the suits don't matter). The player with the greater value takes both of the cards and puts them on the end of their deck.
5. In case the two cards have the same value, the players "go to war":
    - Each of them puts another card, face down, on the other: in order to do that, P1 just has to press "enter" as usual
    - And again each of them puts another card, this time face up, and those cards are compared. 
    - If one of them has greater value, the player who put it takes all of the cards "on the table".
    - If the two cards again have the same values, the players repeat the process: each of them puts one card facing down, and then another facing up and compare them.
    - This process repeats until one player manages to put a card with a bigger value on the table or until at least one of them runs out of cards.
6. The game itself continues until one of the players runs out of cards and looses or, what's more possible, the player(s) get bored and decide to end the game.
