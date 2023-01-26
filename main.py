import random
from game import start, total1, total2
from hit import hit_card
from winloss import winorlose

# deck of cards
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4 , 5 , 6, 7, 8, 9,
       1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4 , 5 , 6, 7, 8, 9,
       "A", "Q", "J", "K","A", "Q", "J", "K","A", "Q", "J", "K","A", "Q", "J", "K",]
random.shuffle(deck)

player = []
dealer = []
# deal
start = start(deck, dealer, player)
choice = input("Do you wish to hit or stand? ").lower()

print(start)
winorlose(player,dealer)
hit_card(deck, choice)
start(player,deck,dealer)
total1(player)
total2(dealer)