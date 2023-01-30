def winorlose(total1, total2):
  if total1 > 21:
    print("Vengeance is an idiot’s game.")
  elif total1 == 21:
    print("Seems like you've won!")
  elif total2 == 21 and total1 > 21:
    print("You sir are a fish.")
  elif total2 > 21:
    print("You don't get to live a bad life and have good things happen to you.")
  elif total2 < 21 and total1 > 21:
    print("You're gonna sleep with your chest open if you ain't careful boy.")
