# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:10:59 2022

@author: RogerTheAlien
"""

# 1 - CREATE A DECK

import random
suits=('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack',
         'Queen','King','Ace')
values= {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,
         'Queen':10,'King':10,'Ace':11}

playing = True
# CREATE A CARD CLASS. WHICH LITERALLY JUST ASSIGNS THE ATRIBUTES OF THE CAD, SUIT, RANK, VALUE. ALSO CHANGES THE
# PRINT VALUE

class Card:
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        
    def __str__ (self):
        return self.rank + ' of ' + self.suit
    
    

# CREATE A DECK CLASS. THIS WILL CREATE A RANDOMISED DECK OF 52 CARDS. 

class Deck:
    def __init__ (self):
        self.deck=[]
        # created an all_cards as a variable of the class. an empty list
        
        for i in suits:
            for j in ranks:
                created_card=Card(i,j)
                self.deck.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()




# CREATE A PLAYER CLASS TO COUNT THE PLAYER'S CHIPS AND BETS

class Player:
    def __init__ (self,name='Dealer',chips=10**10):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.name=name
        self.chips=chips
        self.bet=0
       
        if self.chips<1:
            print(f'\nLooks like {self.name} is bankrupt\n')
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
        
    def player_bet(self,bet):
        self.bet=bet
        if bet > self.chips:
            print("\nOoops, not enough chips in the account!\n")
        else:
            print(f'\nTotal bet is {self.bet}. Remaining chips is: {self.chips-self.bet}\n')
    
    def player_win(self):
        self.chips+=self.bet
        print(f'\n{player_1.name} won {self.bet}. Total chips is: {self.chips}\n')

    def player_lose(self):
        self.chips-=self.bet
        print(f'\n{player_1.name} lose {self.bet}. {self.chips} chips remaining.\n')

    def push(self):
        print("Dealer and Player tie! It's a push.")
            
    def show_cards(self):
        print(f'\n{self.name} has {len(self.cards)} cards:')
        if self.name=='Dealer':
            print("Dealer's Card")               
            for i in range(len(self.cards)-1):
                print(self.cards[i+1])
                
        else:
            for i in range(len(self.cards)):
                print(self.cards[i])
            print(f'Total value is: {self.value}')                
        

def hit(new_deck,player_1):
    
    player_1.add_card(new_deck.deal())
    player_1.adjust_for_ace()


def hit_or_stand(deck,player):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? ")
        if x == 'hit':
            hit(deck,player)
        elif x == 'stand':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break            
     
 
# GAME SET-UP



game_on=True
round_num=0

while game_on:
    round_num+=1
    new_deck=Deck()
    new_deck.shuffle()    
    player_1=Player('Lola', 100)
    player_2=Player()
    print(f'\nRound {round_num}. {player_1.name} has {player_1.chips} chips.\n')
    
    # deal the first two cards each
    player_1.add_card(new_deck.deal())
    player_2.add_card(new_deck.deal())
    player_1.add_card(new_deck.deal())
    player_2.add_card(new_deck.deal())
    
    # take the bet
    player_1.player_bet(int(input(f'\nHow many chips are you betting {player_1.name}?')))

        
    # SHOW THE CARDS
    player_1.show_cards()
    player_2.show_cards()
 

    while playing:          
        hit_or_stand(new_deck,player_1) 
        
        player_1.show_cards()
        player_2.show_cards()
        
        if player_1.value > 21:
            player_1.player_lose()
            break               
    if player_1.value<=21:
        while player_2.value<17:
            hit(new_deck,player_2)
        player_1.show_cards()
        player_2.show_cards()
        if player_2.value>21:
            player_1.player_win()
        elif player_2.value > player_1.value:
            player_1.player_lose()
        elif player_2.value < player_1.value:
            player_1.player_win()
        else:
            player_1.push()
            
    print("\nPlayer's winnings stand at",player_1.chips)
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
