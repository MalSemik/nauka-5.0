import random


class Deck:
    def __init__(self):
        num_cards = [i for i in range(2, 11)]
        all_cards = ((num_cards + ["A", "K", "Q", "J"]) * 4)
        self.my_deck = all_cards
        #print(self.my_deck)

    def shuffle(self):
        random.shuffle(self.my_deck)
        return self.my_deck

    def deal(self, how_many):
        self.how_many = how_many
        cards = []
        for i in range(self.how_many):
            cards.append(self.my_deck.pop(0))
        return cards


class Bank:
    def __init__(self, amount=100):
        self.account = amount

    def withdraw(self, bet):
        self.bet = bet
        self.account -= self.bet
        #print(self.account)

    def deposit(self):
        self.account += self.bet * 2
        print(f"You have {self.account} coins.")


class Player:
    def __init__(self):
        self.bank = Bank()
        #print("Your cards: ", self.hand)

    def receive_cards(self):
        self.hand = my_deck.deal(2)

    def bet(self):
        # dodać try/except na input
        self.my_bet = 0
        while True:
            self.my_bet = int(input(f"You have {self.bank.account} coins. How many would you like to bet? "))
            if self.my_bet > self.bank.account:
                print("Sorry, you don't have enough coins. Bet again.")
                continue
            else:
                print("You bet ", self.my_bet)
                self.bank.withdraw(self.my_bet)
                return False

    def hit(self):
        self.hand.append(my_deck.deal(1)[0])
        print(self.hand)

    def stand(self):
        active_player = swap_players(active_player, players)
        self.active_player = active_player
        return self.active_player

    def count(self):
        value = 0
        for card in self.hand:
            if card not in ["A", "K", "Q", "J"]:
                value += card
            elif card in ["K", "Q", "J"]:
                value += 10
            elif card == "A":
                if value + 10 > 21:
                    value += 1
                else:
                    # for now we will add 10, then maybe player input
                    value += 10

        self.value = value
        # print(self.value)
        return self.value


def swap_players(active_player, players):
    if active_player == players[0]:
        active_player = players[1]
    return active_player


def check_if_21_or_more():
    pass


# Create and shuffle the deck
my_deck = Deck()
my_deck.shuffle()

# Create players, set active player, print players hands
player = Player()
dealer = Player()
players = [player, dealer]
active_player = players[0]
print("Your cards: ", player.hand)
print("Dealers cards:", "[",dealer.hand[0], ", X", "]")
# Ask player how much he wants to bet
player.bet()


# Create game loop
def play(player, dealer, players, active_player):
    winner = False
    while not winner:
        # ask player if they want to hit or stand
        question = input("Do you want to hit (H) or stand (S)?")
        if question.upper() == "H":
            player.hit()
            value = player.count()
            if value > 21:
                print("You loose")
                active_player = players[1]
                winner = True
        if question.upper() == "S":
            # player.stand()
            swap_players(active_player, players)
            while dealer.count() < 17:
                dealer.hit()
                if dealer.count() == 21:
                    winner = True
                if dealer.count() > 21:
                    winner = True

    if active_player == player:
        print("Congratulations! You won!")
        player.bank.deposit()

    return False


game = play(player, dealer, players, active_player)

again = input("Do you want to play again? (Y/N)")
# change to while loop
if again.upper() != "N":
    # Create and shuffle the deck
    my_deck = Deck()
    my_deck.shuffle()

    # Create players, set active player, print players hands
    player = Player()
    dealer = Player()
    players = [player, dealer]
    active_player = players[0]
    print("Your cards: ", player.hand)
    print("Dealers cards:", "[", dealer.hand[0], ", X", "]")
    # Ask player how much he wants to bet
    player.bet()
    game = play(player, dealer, players, active_player=players[0])

print("Goodbye then")