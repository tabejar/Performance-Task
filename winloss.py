def winorlose(player, dealer):
  if player > 21:
    print("Vengeance is an idiot’s game.")
  elif player == 21:
    print("Seems like you've won!")
  elif dealer == 21 and player > 21:
    print("You sir are a fish.")
  elif dealer > 21:
    print("You don't get to live a bad life and have good things happen to you.")
  elif dealer < 21 and player > 21:
    print("You're gonna sleep with your chest open if you ain't careful boy.")
