# TwentyOne 2.0!

# Create a Python module for the card game “Tjugoett” (Blackjack/21).
# The module should include three classes:
# Spelare (Player): describes a general Tjugoett player.
# Användare (User): represents a human player.
# Dator (Computer): represents a computer player.
# The module should also contain a main part that creates the objects and runs the game.

# Purpose of the Exercise (OOP Focus)
# Practice object-oriented programming with inheritance (e.g., User and Computer inherit from Player).
# Encapsulate data and behavior in classes.
# Reuse and extend a base class.
# Combine objects to build a simple interactive card game.

# Twentyone_2_0.py
import CardGame   # import your module that contains new(), give(), and show()

class Player:
    """General player in the Twenty-One game."""
    def __init__(self, deck, name="Player"):
        self.deck = deck
        self.name = name
        self.hand = []
        self.points = 0
        self.num_aces = 0

    def draw_card(self):
        """Draw a new card and update score."""
        card = CardGame.give(self.deck)
        if card is None:
            print("No cards left in the deck!")
            return

        self.hand.append(card)
        suit, rank = card

        # Calculate value of card
        if rank == 1:              # Ace
            self.points += 14
            self.num_aces += 1
        elif rank >= 11:           # J, Q, K
            self.points += 10
        else:
            self.points += rank

        # Adjust Aces if total goes over 21
        while self.points > 21 and self.num_aces > 0:
            self.points -= 13      # Change one Ace from 14 → 1
            self.num_aces -= 1

    def show_cards(self):
        """Display player's cards."""
        for card in self.hand:
            CardGame.show(card, last=" ")
        print("")

    def display_status(self):
        """Print player's current cards and points."""
        print(f"{self.name} has:", end=" ")
        self.show_cards()
        print(f"and {self.points} points.")


class User(Player):
    """Human player."""
    def play(self):
        while True:
            self.draw_card()
            self.display_status()
            if self.points >= 21:
                break
            if not self.keep_playing("One more card?"):
                break
        return self.points

    def keep_playing(self, question):
        answer = input(question + " (y/n): ")
        return len(answer) > 0 and answer[0].lower() == "y"


class Computer(Player):
    """Computer player."""
    def play(self):
        while self.points <= 16:
            self.draw_card()
        self.display_status()
        return self.points


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("Welcome to Twenty-One!")
    deck = CardGame.new()

    while True:
        user = User(deck, "You")
        computer = Computer(deck, "Computer")

        user_points = user.play()
        if user_points > 21:
            print("You busted! Computer wins.")
        else:
            print("\nComputer's turn:")
            comp_points = computer.play()
            if comp_points > 21 or user_points > comp_points:
                print("You win! 🎉")
            elif comp_points == user_points:
                print("It's a tie – computer wins by rule!")
            else:
                print("Computer wins!")

        if not user.keep_playing("\nPlay another round?"):
            break


#BONUS to exercise 21:
# Change in the main-part of the program so that två human players can play against each other

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("Welcome to Twenty-One!")
    deck = CardGame.new()

    while True:
        # Create two human players
        player1 = User(deck, "Player 1")
        player2 = User(deck, "Player 2")

        print("\n--- Player 1's turn ---")
        p1_points = player1.play()
        if p1_points > 21:
            print("Player 1 busted!")

        print("\n--- Player 2's turn ---")
        p2_points = player2.play()
        if p2_points > 21:
            print("Player 2 busted!")

        # Determine winner
        print("\n--- Round Results ---")
        if p1_points > 21 and p2_points > 21:
            print("Both players busted! No winner.")
        elif p1_points > 21:
            print("Player 2 wins! 🎉")
        elif p2_points > 21:
            print("Player 1 wins! 🎉")
        elif p1_points > p2_points:
            print("Player 1 wins! 🎉")
        elif p2_points > p1_points:
            print("Player 2 wins! 🎉")
        else:
            print("It's a tie!")

        # Ask if players want another round
        if not player1.keep_playing("\nPlay another round?"):
            break

