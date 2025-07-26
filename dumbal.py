from random import shuffle,randint

class Dumbal:
    # initializing all the cards according to their types and storing them in list
    diamonds = ('A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦')
    hearts = ('A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥')
    clubs = ('A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣')
    spades = ('A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠')

    def __init__(self):
        self.deck = []
        self.floor = []
        self.create_deck()
        self.shuffle_deck()
        self.game()

    def create_deck(self):
        """ function to create deck using all the cards """
        self.deck.extend(self.diamonds + self.clubs + self.hearts + self.spades)

    def shuffle_deck(self):
        """ function to shuffle deck """
        shuffle(self.deck)
        # for i in range(len(self.deck)): could be done this way as well
            # self.deck[i] = self.deck[randint(0,51)]

    def game(self):
        """ 
        function to initialize the game. 
        creates two players with 5 cards from the deck 
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

        print('-'*40)
        print("Your cards in hand:")
        for each in player: print(each, end="\t")
        print('\n'+'-'*40)

        play_continue = True
        while play_continue == True:
            throw = int(input("\nProvide index of the card you want to throw: "))
            if throw <= len(player):
                self.throw_card(throw,player)
            else:
                print("Invalid card!")
            for each in player: print(each, end="\t")

            print(f"\nYou picked: {self.pick_card(player)}")

            # bots' playing turns, throw at random and pick 
            self.throw_card(randint(0,len(bot1)),bot1)
            self.pick_card(bot1)
            for each in bot1: print(each, end="\t")
            print('\n')

            self.throw_card(randint(0,len(bot2)),bot2)
            self.pick_card(bot2)
            for each in bot2: print(each, end="\t")
            print('\n')

            self.throw_card(randint(0,len(bot3)),bot3)
            self.pick_card(bot3)
            for each in bot3: print(each, end="\t")
            print('\n')

            self.throw_card(randint(0,len(bot4)),bot4)
            self.pick_card(bot4)
            for each in bot4: print(each, end="\t")
            print('\n')

            complete = input("Do you want to complete the game?(y/n)")
            if complete.strip().lower() == 'y':
                self.complete_game(player)
            elif complete.strip().lower() == 'n':
                continue
            else:
                print("Invalid input.")
    
    def pick_card(self, player_cards):
        """
        function to let players pick card from their hand
        """
        picked_card = self.deck.pop(0)
        player_cards.append(picked_card)
        return picked_card

    def throw_card(self, i, player_cards):
        """
        function to let players throw cards from their hand
        """

        if 0 <= i < len(player_cards):
            selected_card = player_cards[i]
            selected_value = selected_card[:-1]

            # if there are similar cards in hand 
            duplicates = [card for card in player_cards if card[:-1] == selected_value]

            # alternate method to find duplicates
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
                print(f"Thrown duplicates: {duplicates}")
            else:
                # Throw just the selected card
                self.floor.append(player_cards.pop(i))
                print(f"Thrown single card: {selected_card}")

            print("Floor:", self.floor) 
    
    def complete_game(self, player_cards):
        # if total in hand of a player is less than 10, the player wins the game.
        total_in_hand = 0
        # calcutating sum of all cards of the player's hand
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

        if total_in_hand <= 10:
            print(f"You have: {total_in_hand}, You've won the game!")
        else:
            print(f"You have: { total_in_hand }, You're not eligible to complete the game!")

Dumbal()