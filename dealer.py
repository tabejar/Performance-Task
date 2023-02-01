import random
def dealerhit(dealer,deck):
  dealertotal = sum(dealer)
  if dealertotal < 18:
    card = random.choice(deck)
    dealer.append(card)
    deck.remove(card)
    print("dealer has hit")
    print("dealer has: " + str(dealer))