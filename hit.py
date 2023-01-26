from game import deal
def hit_card(deck, choice, player):
  if choice == "hit":
   deal(player, deck)
   print()
  else:
    print("have it your way...")
