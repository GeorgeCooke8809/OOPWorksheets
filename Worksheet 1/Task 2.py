# Task 9.5
import random

class Deck:
    cards = [suit + number for suit in "HCDS" for number in "123456789JQKA"]
    next_card_no = 0

    def __init__(self):
        if Deck.next_card_no == 0:
            random.shuffle(Deck.cards)

        if not Deck.cards:
            print("No more cards")
        else:
            self.card_description = Deck.cards.pop()
            self.card_no = Deck.next_card_no

            Deck.next_card_no += 1

deck1 = []

for card_no in range(10):
    card = Deck()
    deck1.append(card)

print("Player 1:")
for card in deck1:
    print("Card No", card.card_no, "Description", card.card_description)


deck2 = []

for card_no in range(10):
    card = Deck()
    deck2.append(card)

print("\nPlayer 2:")
for card in deck2:
    print("Card No", card.card_no, "Description", card.card_description)