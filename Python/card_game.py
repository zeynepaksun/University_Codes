import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)


class Card:
    def __init__(self, num_players):
        if num_players != 2 and num_players != 4:
            raise ValueError("Number of players must be 2 or 4.")
        self.num_players = num_players
        self.players_decks = [deck[i::num_players] for i in range(num_players)]
        self.player_scores = [0] * num_players

    def play(self):
        while all(len(deck) > 0 for deck in self.players_decks):
            self.play_round()

        self.determine_winner()

    def play_round(self):
        played_cards = [deck.pop(0) if len(deck) > 0 else None for deck in self.players_decks]
        for player, card in enumerate(played_cards):
            if card:
                print(f"Player {player+1}: {card}")

        highest_rank = max(card[0] for card in played_cards if card)
        winning_players = [i for i, card in enumerate(played_cards) if card and card[0] == highest_rank]

        if len(winning_players) == 1:
            self.player_scores[winning_players[0]] += 1
        else:
            print("No winner")
            if self.num_players == 2:
                if len(self.players_decks[0]) < 3 or len(self.players_decks[1]) < 3:
                    print("Not enough cards")
                    return
                for i in range(self.num_players):
                    for _ in range(3):
                        self.players_decks[i].pop(0)
            elif self.num_players == 4:
                for i in range(self.num_players):
                    if len(self.players_decks[i]) < 2:
                        print(f"Not enough cards for Player {i+1}")
                        return
                    self.players_decks[i].pop(0)

    def determine_winner(self):
        max_score = max(self.player_scores)
        winners = [i+1 for i, score in enumerate(self.player_scores) if score == max_score]

        if len(winners) == 1:
            print(f"Player {winners[0]} won")
        else:
            print("It's a tie")


class TwoPlayerCardGame(Card):
    def __init__(self):
        super().__init__(2)


class FourPlayerCardGame(Card):
    def __init__(self):
        super().__init__(4)



game_2_players = TwoPlayerCardGame()
game_2_players.play()

print("-----------")


game_4_players = FourPlayerCardGame()
game_4_players.play()
