import random 

# deals 2 cards to both the player and dealer
def start(deck, player, dealer):
  card = random.choice(deck)
  player.append(card)
  deck.remove(card)
  card = random.choice(deck)
  player.append(card)
  deck.remove(card)
  card = random.choice(deck)
  dealer.append(card)
  deck.remove(card)
  card = random.choice(deck)
  dealer.append(card)
  deck.remove(card)
  print(player)

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
