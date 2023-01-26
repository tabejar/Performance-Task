import random
from game import start, hit_card, total1, total2
from winloss import winorlose

# deck of cards
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4 , 5 , 6, 7, 8, 9,
       1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4 , 5 , 6, 7, 8, 9,
       "A", "Q", "J", "K","A", "Q", "J", "K","A", "Q", "J", "K","A", "Q", "J", "K",]
random.shuffle(deck)

player = []
dealer = []
#deals cards
start = start(deck, dealer, player)
choice = input("Do you wish to hit or stand? ").lower()
hit_card(deck, choice, player)

