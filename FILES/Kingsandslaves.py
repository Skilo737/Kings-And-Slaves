
import pygame
from livewires import games

class CardImage(games.Sprite):
   """A playing card. """
   SUITS = ["s", "c", "d", "h"]
   RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]   
   def __init__(self, rank, suit, face_up = True):
      self.suit = suit
      self.rank = rank
      self.is_face_up = face_up
      if self.suit == "s":
         if self.rank == "A":
            self.image = games.load_image("as-pixilart.png")
         elif self.rank == "2":
            self.image = games.load_image("2s-pixilart.png")
         elif self.rank == "3":
            self.image = games.load_image("3s-pixilart.png")
         elif self.rank == "4":
            self.image = games.load_image("4s-pixilart.png")
         elif self.rank == "5":
            self.image = games.load_image("5s-pixilart.png") 
         elif self.rank == "6":
            self.image = games.load_image("6s-pixilart.png")
         elif self.rank == "7":
            self.image = games.load_image("7s-pixilart.png")
         elif self.rank == "8":
            self.image = games.load_image("8s-pixilart.png") 
         elif self.rank == "9":
            self.image = games.load_image("9s-pixilart.png")
         elif self.rank == "10":
            self.image = games.load_image("10s-pixilart.png") 
         elif self.rank == "J":
            self.image = games.load_image("js-pixilart.png")          
         elif self.rank == "Q":
            self.image = games.load_image("qs-pixilart.png") 
         elif self.rank == "K":
            self.image = games.load_image("Ks-pixilart.png") 
      elif self.suit == "c":
         if self.rank == "A":
            self.image = games.load_image("ac-pixilart.png")
         elif self.rank == "2":
            self.image = games.load_image("2c-pixilart.png")
         elif self.rank == "3":
            self.image = games.load_image("3c-pixilart.png")
         elif self.rank == "4":
            self.image = games.load_image("4c-pixilart.png")
         elif self.rank == "5":
            self.image = games.load_image("5c-pixilart.png")
         elif self.rank == "6":
            self.image = games.load_image("6c-pixilart.png")
         elif self.rank == "7":
            self.image = games.load_image("7c-pixilart.png")
         elif self.rank == "8":
            self.image = games.load_image("8c-pixilart.png")
         elif self.rank == "9":
            self.image = games.load_image("9c-pixilart.png")
         elif self.rank == "10":
            self.image = games.load_image("10c-pixilart.png")
         elif self.rank == "10":
            self.image = games.load_image("jc-pixilart.png")      
         elif self.rank == "Q":
            self.image = games.load_image("qc-pixilart.png")
         elif self.rank == "K":
            self.image = games.load_image("kc-pixilart.png")
      elif self.suit == "d":
         if self.rank == "A":
            self.image = games.load_image("ad-pixilart.png")
         elif self.rank == "2":
            self.image = games.load_image("2d-pixilart.png")
         elif self.rank == "3":
            self.image = games.load_image("3d-pixilart.png")
         elif self.rank == "4":
            self.image = games.load_image("4d-pixilart.png")
         elif self.rank == "5":
            self.image = games.load_image("5d-pixilart.png")
         elif self.rank == "6":
            self.image = games.load_image("6d-pixilart.png")
         elif self.rank == "7":
            self.image = games.load_image("7d-pixilart.png")
         elif self.rank == "8":
            self.image = games.load_image("8d-pixilart.png")
         elif self.rank == "9":
            self.image = games.load_image("9d-pixilart.png")
         elif self.rank == "10":
            self.image = games.load_image("10d-pixilart.png") 
         elif self.rank == "J":
            self.image = games.load_image("jd-pixilart.png")          
         elif self.rank == "Q":
            self.image = games.load_image("qd-pixilart.png") 
         elif self.rank == "K":
            self.image = games.load_image("kd-pixilart.png")
      elif self.suit == "h":
         if self.rank == "A":
            self.image = games.load_image("ah-pixilart.png")
         elif self.rank == "2":
            self.image = games.load_image("2h-pixilart.png")
         elif self.rank == "3":
            self.image = games.load_image("3h-pixilart.png")
         elif self.rank == "4":
            self.image = games.load_image("4h-pixilart.png")
         elif self.rank == "5":
            self.image = games.load_image("5h-pixilart.png") 
         elif self.rank == "6":
            self.image = games.load_image("6h-pixilart.png")
         elif self.rank == "7":
            self.image = games.load_image("7h-pixilart.png")
         elif self.rank == "8":
            self.image = games.load_image("8h-pixilart.png") 
         elif self.rank == "9":
            self.image = games.load_image("9h-pixilart.png")
         elif self.rank == "10":
            self.image = games.load_image("10h-pixilart.png") 
         elif self.rank == "J":
            self.image = games.load_image("jh-pixilart.png")          
         elif self.rank == "Q":
            self.image = games.load_image("qh-pixilart.png") 
         elif self.rank == "K":
            self.image = games.load_image("kh-pixilart.png")
      super(Card, self).__init__(image = self.image, x = games.screen.width//2, y = games.screen.height//2)
   def flip(self):
      if self.is_face_up:
         super(Card, self).__init__(image = games.load_image("card-backside.png"), x = games.screen.width//2, y = games.screen.height//2)
      else:
         super(Card, self).__init__(image = self.image, x = games.screen.width//2, y = games.screen.height//2)
      self.is_face_up = not self.is_face_up
                  
   
class Card(object):
   """A playing card. """
   SUITS = ["s", "c", "d", "h"]
   RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]   
   def __init__(self, rank, suit, face_up = True):
      self.suit = suit
      self.rank = rank
      self.is_face_up = face_up
   def __str__(self):
      if self.is_face_up:
         rep = self.rank + self.suit
      else:
         rep = "[XX]"
      return rep
      
   def flip(self):
      self.is_face_up = not self.is_face_up    
   
   
class Hand(object):
   """ A hand of playing cards. """
   def __init__(self):
      self.cards = []
      
   def __str__(self):
      if self.cards:
         rep = ""
         for card in self.cards:
            rep += str(card) + "\t"
      else:
         rep = "empty"
      return rep               
   def clear(self):
      self.cards = []
      
      
   def add(self, card):
      self.cards.append(card)
   def give(self, card, dest):
      self.cards.remove(card)
      dest.add(card)
         
         
         
         
class Deck(Hand):
   """ A deck of playing cards. """
   def populate(self):
      for suit in Card.SUITS:
         for rank in Card.RANKS:
            self.add(Card(rank, suit))
            
   def shuffle(self):
      import random
      random.shuffle(self.cards)
      
   def deal(self, hands, amnt = 7):
      for round in range(amnt):
         for hand in hands:
            if self.cards:
               top_card = self.cards[0]
               self.give(top_card, hand)
            else:
               print("Can't continue to deal. Out of cards.")


games.init(screen_width = 640, screen_height = 480, fps = 60)

def setup():
   no_players = 4
   no_cards = 13
   
   my_deck = Deck()
   my_deck.populate()
   my_deck.shuffle()
   hand_list = []
   for player in range(no_players):
      hand_list.append(Hand())
   my_deck.deal(hand_list, no_cards)
   
   for hand in hand_list:
      print (hand)
      print ()
   

def main():
   wall_image = games.load_image(("Cardsbackdrop.jpg"), transparent = False)
   games.screen.background = wall_image
   
   setup()
    
   card = Card("A", "c")
   cardsprite = CardImage("A", "c")
   games.screen.add(cardsprite)
   
 
   
   games.screen.mainloop()


main()