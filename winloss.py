# counts up the total for both players and decides the winner
def winorlose(player, dealer):
  total = 0 
  playercount = sum(player)
  total1 = total + playercount
  print("player: " + str(total1))
  total0 = 0 
  dealercount = sum(dealer)
  total2 = total0 + dealercount
  print("dealer: " + str(total2))
  if total1 < total2 and total2 < 21:
    print("Apex Legends is an idiot’s game.")
  elif total1 > total2 and total1 < 22:
    print("Victory Royale!")
  elif total2 == 21 and total1 < 21:
    print("You sir are a fishstick.")
  elif total2 < 21 and total1 > 21:
    print("You're gonna sleep with your chest looted if you ain't careful boy.")
  elif total2 > 21 and total1 < 21:
    print("Five thousand vbucks? Lost...")



