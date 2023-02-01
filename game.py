import random 

# deals 2 cards to both the player and dealer and prints their hands
def start(deck, player, dealer):
  for i in range(2):
    card = random.choice(deck)
    player.append(card)
    deck.remove(card)
  for i in range(2):
    card = random.choice(deck)
    dealer.append(card)
    deck.remove(card)
  print("Dealer has: " + str(player))
  print("You have: " + str(dealer))

#code to deal a card to the player if they wish to hit
def deal(player, deck):
  card = random.choice(deck)
  player.append(card)
  deck.remove(card)
  
#determines whether the player input was to hit or stand
def hit_card(deck, choice, player):
  if choice == "hit":
    deal(player, deck)
    print(f"your new hand is {player}")
  else:
    print("have it your way...")
