"""
War Gane
Warm up project - No real players. 2 CPU will battle
"""

# CARD
# SUIT, RANK, VALUE

import random

suits = (
    "Hearts",
    "Diamonds",
    "Spades",
    "Clubs",
)

ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
# Dictionary for card values
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class Card:
    """
    Make all card types in deck
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """
    Create the deck of cards and shuffle contents. Get one from the deck
    """

    def __init__(self):
        # Happens at the start. just to make a list with all the cards.
        self.all_cards = []

        # Creates the deck of cards
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)  # Add each card in the list.

    # Re-arrange cards in the list
    def shuffle(self):
        random.shuffle(self.all_cards)

    # We remove one card from all_cards.
    def deal_one(self):
        return self.all_cards.pop()


class Player:
    """
    Create the deck of cards and shuffle contents. Get one from the deck
    """

    def __init__(self, name):
        self.name = name

        # new player has no cards
        self.all_cards = []

    def remove_one(self):
        # remove first card since that's the top.
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # add new cards to the players deck. Cards are added at the end of the list.
        # check if new_cards is a list of new cards or just 1 card.
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)  # use extend if it's a list of cards
        else:
            self.all_cards.append(new_cards)  # use append if only 1 card

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


##### GAME SETUP

# Create Deck and Players set of cards
new_deck = Deck()
new_deck.shuffle()  # shuffle the constructed deck

player1_deck = Player("Ray")
player2_deck = Player("Genny")

# print(len(new_deck.all_cards))  # 52 cards
# print(len(player1_deck.all_cards))  # 0
# print(len(player2_deck.all_cards))  # 0

# Divide the shuffled deck to 2 players. 52 / 2 = 26
for x in range(26):
    player1_deck.add_cards(new_deck.deal_one())
    player2_deck.add_cards(new_deck.deal_one())

# print(len(new_deck.all_cards))  # 0 cards
# print(len(player1_deck.all_cards))  # 26 cards
# print(len(player2_deck.all_cards))  # 26 cards

# Gameplay
import pdb

game_on = True
round_num = 0
war_count = 0

while game_on:
    round_num += 1
    # print(
    #     f"Round {round_num} : Player 1 : {len(player1_deck.all_cards)}, Player 2 : {len(player2_deck.all_cards)}"
    # )

    # Check if players still have cards.
    if len(player1_deck.all_cards) == 0:
        print(
            f"Game Over! Player 1 {player1_deck.name} has no more cards, Player 2 {player2_deck.name} wins"
        )
        game_on = False
        break

    if len(player2_deck.all_cards) == 0:
        print(
            f"Game Over! Player 2 {player2_deck.name} has no more cards, Player 1 {player1_deck.name} wins"
        )
        game_on = False
        break

    # Game continues if both players still have cards.
    # Start a round. Reset each player's card on the table each round.
    # Use a list because during war, more than one card will be here.
    player1_roundcards = []
    player2_roundcards = []

    # get top card from player's half of the deck and add into round card list.
    player1_roundcards.append(player1_deck.remove_one())
    player2_roundcards.append(player2_deck.remove_one())

    table_card_compare = True

    # Comparing hand of player1 and player2
    while table_card_compare:
        # print(player1_roundcards[-1].value)
        # print(player2_roundcards[-1].value)
        # Get card at -1 position of the list.
        if player1_roundcards[-1].value > player2_roundcards[-1].value:
            # Player 1 will get ALL the cards on the table
            player1_deck.add_cards(player1_roundcards)
            player1_deck.add_cards(player2_roundcards)

            table_card_compare = False  # end round

        elif player1_roundcards[-1].value < player2_roundcards[-1].value:
            # Player 2 will get ALL the cards on the table
            player2_deck.add_cards(player1_roundcards)
            player2_deck.add_cards(player2_roundcards)

            table_card_compare = False  # end round

        else:
            # if cards are equal, player will draw more cards. The last card will be compared again.
            # Whoever wins will take all clounds on the table.
            print("Cards are equal! WAR!!")
            war_count += 1

            # Check first if players can provide the required number of cards during WAR. If not, they lose.
            if len(player1_deck.all_cards) < 5:  # Bigger value means shorter game
                print(f"Player 1 {player1_deck.name} has insufficient cards.")
                print(f"Game Over! Player 2 {player2_deck.name} WINS!")
                game_on = False
                break

            elif len(player2_deck.all_cards) < 5:  # Bigger value means shorter game
                print(f"Player 2 {player2_deck.name} has insufficient cards.")
                print(f"Game Over! Player 1 {player1_deck.name} WINS!")
                game_on = False
                break

            else:
                # Continue the war
                # Get top card from player's half of the deck and add into round card list.
                for num in range(5):  # Bigger value means shorter game
                    player1_roundcards.append(player1_deck.remove_one())
                    player2_roundcards.append(player2_deck.remove_one())


print(f"Total Rounds : {round_num}")
print(f"Total Wars : {war_count}")
