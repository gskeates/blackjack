import random

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
names  = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}


class Card:
    def __init__(self, suit, index):
        self.suit = suit
        self.index = index
        self.value = min(index, 10)
        self.name = index if index not in names.keys() else names[index]

    def disp(self):
        print('{} of {}'.format(self.name, self.suit))


class Deck:
    def __init__(self):
        self.cards = [ Card(suit, index) for suit in suits for index in range(1, 14) ]

    def replenish(self):
        self.cards = [ Card(suit, index) for suit in suits for index in range(1, 14) ]

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, is_bot):
        self.is_bot = is_bot
        self.cards = list()
        self.value = sum(card.value for card in self.cards)
        self.score = 0

    def clear(self):
        self.cards = list()

def deal_card(player, display=True):
    card = random.choose(deck.cards.pop())
    player.cards.append(card)
    if display and player.is_bot:
        print("The dealer has been dealt the {} of {}".format(card.name, card.suit))
    elif display:
        print("You have been dealt the {} of {}".format(card.name, card.suit))

deck = Deck()
deck.shuffle()

game_over = False

while not game_over:
    episode_over = False

    # Shuffle deck
    deck.replenish()
    deck.shuffle()

    while not episode_over:
        deal_card(player)
        deal_card(player)

        deal_card(dealer)
        deal_card(dealer, display=False)

        # Draw
        if dealer.value == 21 and player.value == 21:
            print("Draw!")
            episode_over = True

        # Player wins
        elif player.value == 21:
            print("You win!")
            player.score += 1
            episode_over = True

        # Start drawing cards

        player_done = False

        while not player_done:
            # Get input from player
            while True:
                response = input("Hit? [y/n]: ").lower()

                if response not in ['y', 'n']:
                    print("Sorry, I couldn't understand that.")
                else:
                    break

            if response == 'y':
                deal_card(player)

                if player.value > 21:
                    print("Sorry, you've gone bust")

                    player.score -= 1
                    player_done = True
                    episode_over = True

                elif player.value == 21:
                    print("You win!")
                    player.score += 1
                    episode_over = True

            else:
                player_done = True


        player.clear()
        dealer.clear()
