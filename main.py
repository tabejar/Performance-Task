import random
from game import start, hit_card
from winloss import winorlose
from dealer import dealerhit

# deck of cards
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4 , 5 , 6, 7, 8, 9,
       1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4 , 5 , 6, 7, 8, 9,]
random.shuffle(deck)
print("welcome to Simplejack! The simple version of BlackJack.")
print("This is a game of BlackJack without any Ace's,")
print("Jack's, King's, or Queen's!")
print(" ")
player = []
dealer = []
#deals cards
start = start(deck, dealer, player)
print(" ")
#asks the player if they wish to hit for another
#card or to keep their hand
choice = input("Do you wish to hit or stand? ").lower()
print(" ")
hit_card(deck, choice, player)
print("")
#dealer hits depending on their hand
dealerhit(dealer, deck)
print(" ")
winorlose(player, dealer)