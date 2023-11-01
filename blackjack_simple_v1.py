"""
BlackJack

Game Play
To play a hand of Blackjack the following steps must be followed:
1. Create a deck of 52 cards - OK
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again
"""
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
    Make all card types in deck.
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """
    Each card is created and compiled in self.deck
    Each card has a suit and rank
    """

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "Deck has : " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    """
    Check sum of current hand. Check if there are aces and adjust sum
    """

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # card passed on
        # from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]  # get the rank part of the tupple

    def adjust_for_ace(self):
        # If total value > 21 and I still have an ace
        # then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    """
    Set total chips. Add or subtract bet and update the total
    """

    # Total current chip value
    def __init__(self, total=100):
        self.total = total  # total by default is 100.
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    """
    Function to take user defined bet but confirm first if there's enough chips remaining.
    """
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(
                    f"Sorry, you have insufficient chips. Current total is : {chips.total}"
                )
            else:
                break


def hit(deck, hand):
    """
    Get a card from the deck then add it to your total. adjust for aces.
    """
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """
    Ask user if hit or stand.
    """
    global playing  # to control an upcoming while loop

    while True:
        x = input("Hit or Stand, (Enter h or s) : ")

        # To make sure that user entry will be accepted regarless is upper or lower case h or s.
        # Check first charcter of the string.
        if x[0].lower() == "h":
            hit(deck, hand)  # add card to hand

        elif x[0].lower() == "s":
            print("Player stands. Dealer with now play")
            playing = False

        else:
            print("Sorry, please enter 'h' or 's' only")
            continue
        break  # Escape while loop


def show_some(player, dealer):
    """
    Show 1 card of the dealer and player's cards.
    """
    # dealer.cards[1]

    # Show only ONE of the dealer's cards.
    print("\nDealer's Hand: ")
    print("First Card hidden!")
    print(dealer.cards[1])  # the second card of the dealer.

    # Show all (2 cards) of the player's hand/cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    # print("\nPlayer's Hand:", *player.cards, sep='\n ')

    # OR

    # print("\nDealer's Hand:")
    # print(" <card hidden>")
    # print('',dealer.cards[1])
    # print("\nPlayer's Hand:", *player.cards, sep='\n ')
    # like looping using this asterisk.
    # sep is "separator" character


def show_all(player, dealer):
    """
    Show all cards of the dealer and player's cards
    """
    # show all the dealer's cards

    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)
    # calcuilate the display value (ex. Jack + King = 20)
    print(f"Value of Dealer's hand is : {dealer.value}")

    # Show all of the player's hand/cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is : {player.value}")
    # show all the player's cards

    # OR
    # print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    # print("Dealer's Hand =",dealer.value)
    # print("\nPlayer's Hand:", *player.cards, sep='\n ')
    # print("Player's Hand =",player.value)


# Example of using *items
# items = [1,2,3]
#
# print("Items are : ", *items, sep=" a ")
# output = Items are :  a 1 a 2 a 3


def player_busts(player, dealer, chips):
    print("BUST Player!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer Busts! Player Wins!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()


def push(player, dealer, chips):
    print("Dealer and player TIE! Push!")


## MAIN ##
while True:
    # Print an opening statement
    print("WELCOME TO BLACKJACK")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())  # init card1
    player_hand.add_card(deck.deal())  # init card2

    # for card in player_hand.cards:  # debug lines to check drawn card
    #    print(card)

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())  # init card1
    dealer_hand.add_card(deck.deal())  # init card2

    # for card in dealer_hand.cards:  # debug lines to check drawn card
    #    print(card)

    # Set up the Player's chips
    player_chips = Chips()  # default value of 100 will be used
    # player_chips = Chips(500)

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    playing = True

    while playing:  # recall this global variable from our hit_or_stand function.
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f"\nPlayer Total Chips : {player_chips.total}")

    # Ask to play again
    new_game = input("Would you like to play another hand? y/n: ")

    if new_game[0].lower == "y":
        playing = True
        continue
    else:
        print("Thank you for playing!")

    break
