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

        play_continue = True
        while play_continue == True:
            throw = int(input("\nProvide index of the card you want to throw: "))
            if throw <= len(player):
                self.throw_card(throw,player)
            else:
                print("Invalid card!")

            print(f"\nYou picked: {self.pick_card(player)}")
            print('\n'+'-'*45)
            print("Your Hand: ",end='\t')
            for each in player: print(each, end="\t")
            print('\n'+'-'*45)

            # bots' playing turns, throw at random and pick 
            self.throw_card(randint(0,len(bot1)-1),bot1)
            self.pick_card(bot1)
            print("Bot1's Hand: ",end='\t')
            for each in bot1: print(each, end="\t")
            if self.complete_game(bot1) <= 10:
                print("\nBot1 has won the game.")
                play_continue = False

            self.throw_card(randint(0,len(bot1)-1),bot2)
            self.pick_card(bot2)
            print("Bot2's Hand: ",end='\t')
            for each in bot2: print(each, end="\t")
            if self.complete_game(bot2) <= 10:
                print("\nBot1 has won the game.")
                play_continue = False

            self.throw_card(randint(0,len(bot1)-1),bot3)
            self.pick_card(bot3)
            print("Bot3's Hand: ",end='\t')
            for each in bot3: print(each, end="\t")
            if self.complete_game(bot3) <= 10:
                print("\nBot1 has won the game.")
                play_continue = False

            self.throw_card(randint(0,len(bot1)-1),bot4)
            self.pick_card(bot4)
            print("Bot4's Hand: ",end='\t')
            for each in bot4: print(each, end="\t")
            if self.complete_game(bot4) <= 10:
                print("\nBot1 has won the game.")
                play_continue = False


            print("\nFloor:", self.floor) 

            complete = input("Do you want to complete the game?(y/n)")
            if complete.strip().lower() == 'y':
                if self.complete_game(player) <= 10:
                    print("You have won the game!")
                else:
                    print("Not eligible to end the game!")
                play_continue = False
            elif complete.strip().lower() == 'n':
                continue
            else:
                print("Invalid input.")
    
    def pick_card(self, player_cards):
        """
        function: let players pick card from their hand
        """
        picked_card = self.deck.pop(0)
        player_cards.append(picked_card)
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
                # print(f"Thrown duplicates: {duplicates}")
            else:
                # Throw just the selected card
                self.floor.append(player_cards.pop(i))
                # print(f"Thrown single card: {selected_card}")
    
    def complete_game(self, player_cards):
        """
        function: if total in hand of a player is less than 10, the player wins the game.
        """
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
        return total_in_hand

        # if total_in_hand <= 10:
        #     print(f"You have: {total_in_hand}, You've won the game!")
        # else:
        #     print(f"You have: { total_in_hand }, You're not eligible to complete the game!")

Dumbal()