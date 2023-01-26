import random 

# deals 2 cards to both the player and dealer
def start(deck, player, dealer):
  for i in range(2):
    card = random.choice(deck)
    player.append(card)
    deck.remove(card)
  for i in range(2):
    card = random.choice(deck)
    dealer.append(card)
    deck.remove(card)
  print(player)
  print(dealer)

def deal(player, deck):
  card = random.choice(deck)
  player.append(card)
  deck.remove(card)
  
# counts up the total for the player
def total1(player):
  total = 0 
  playercount = sum(player)
  total = total + playercount

# counts up the total for the dealer
def total2(dealer):
  total = 0 
  dealercount = sum(dealer)
  total = total + dealercount

def hit_card(deck, choice, player):
  if choice == "hit":
    deal(player, deck)
    print(f"your new hand is {player}")
  else:
    print("have it your way...")
