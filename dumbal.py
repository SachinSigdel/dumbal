from random import shuffle,randint

class Dumbal:
    # initializing all the cards according to their types and storing them in list
    diamonds = ('A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦')
    hearts = ('A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥')
    clubs = ('A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣')
    spades = ('A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠')
    play_continue = True

    def __init__(self):
        self.deck = []
        self.floor = []
        self.create_deck()
        self.shuffle_deck()
        self.game()

    def create_deck(self):
        """ function: create deck using all the cards """
        self.deck.extend(self.diamonds + self.clubs + self.hearts + self.spades)

    def shuffle_deck(self):
        """ function: shuffle deck """
        shuffle(self.deck)
        # for i in range(len(self.deck)): could be done this way as well
            # self.deck[i] = self.deck[randint(0,51)]

    def game(self):
        """ 
        function: initialize the game and create two players with 5 cards from the deck 
        """
        player = []
        bot1 = []
        bot2 = []
        bot3 = []
        bot4 = []
        for _ in range(5):
            # assigning cards to the players
            player.append(self.deck.pop(0))
            bot1.append(self.deck.pop(0))
            bot2.append(self.deck.pop(0))
            bot3.append(self.deck.pop(0))
            bot4.append(self.deck.pop(0))

        print('-'*45)
        print("Hand: ",end='\t')
        for each in player: print(each, end="\t")
        print('\n'+'-'*45)

        while self.play_continue:
            try:
                throw = int(input("\nProvide the index of the card you want to throw: "))
                if 0 <= throw < len(player):
                    self.throw_card(throw,player)
                else:
                    print("Invalid card!")
                    continue
            except ValueError:
                print("\n Please provide a valid card!")
                continue

            print(f"\nYou picked: {self.pick_card(player)}")
            print('\n'+'-'*45)
            print("Your Hand: ",end='\t')
            for each in player: print(each, end="\t")
            print('\n'+'-'*45)

            complete = input("Do you want to complete the game?(y/n)")
            if complete.strip().lower() == 'y':
                if self.return_total(player) <= 10:
                    print("You have won the game!")
                    self.play_continue = False
                else:
                    print("Not eligible to end the game!")
                    continue
            elif complete.strip().lower() == 'n':
                self.play_continue = True
            else:
                print("Invalid input.")
                continue

            # bots' playing turns, throw at random and pick
            self.bot_game(bot1)
            self.bot_game(bot2)
            self.bot_game(bot3)
            self.bot_game(bot4)

            print("\nFloor:", self.floor)
    
    def pick_card(self, player_cards):
        """
        function: let players pick card from their hand
        """
        picked_card = self.deck.pop(0)
        if self.deck:
            player_cards.append(picked_card)
        else:
            self.deck.extend(self.floor)
            self.floor.clear()
            print("Deck recreated using cards in floor!")
            self.shuffle_deck()
        return picked_card

    def throw_card(self, i, player_cards):
        """
        function: let players throw cards from their hand
        """
        if 0 <= i < len(player_cards):
            selected_card = player_cards[i]
            selected_value = selected_card[:-1]

            # if there are similar cards in hand 
            duplicates = [card for card in player_cards if card[:-1] == selected_value]

            # alternate method to find duplicate cards
            # duplicates = []
            # for each in player_cards:
            #     if each[:-1] == selected_value:
            #         duplicates.append(each)
            # print("Duplicates:",duplicates)

            if len(duplicates) > 1:
                # throw to floor
                for card in duplicates:
                    self.floor.append(card)
                    player_cards.remove(card)
            else:
                # Throw just the selected card
                self.floor.append(player_cards.pop(i))

    def bot_game(self, bot):
        self.throw_card(randint(0, len(bot) - 1), bot)
        self.pick_card(bot)
        print("\nBot's Hand: ", end='\t')
        for each in bot: print(each, end="\t")
        if self.return_total(bot) <= 10:
            print("\nBot has won the game.")
            self.play_continue = False

    def return_total(self, player_cards):
        """
        function: if total in hand of a player is less than 10, the player wins the game.
        """
        total_in_hand = 0
        # calculating sum of all cards of the player's hand
        for i in range(len(player_cards)):
            num_value = player_cards[i][:-1]
            # assigning values to Alphabet cards.
            if num_value == 'A':
                total_in_hand += 1
            elif num_value == 'J':
                total_in_hand += 11
            elif num_value == 'Q':
                total_in_hand += 12
            elif num_value == 'K':
                total_in_hand += 13
            else:
                total_in_hand += int(player_cards[i][:-1])
        return total_in_hand

Dumbal()