#Treely Dowd - 12/9/19

# Cards Module
# Basic classes for a game with playing cards
from livewires import games 

class Card(object):
   """A playing card. """
   SUITS = ["s", "c", "d", "h"]
   RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]   
   def __init__(self, rank, suit, face_up = True):
      self.suit = suit
      self.rank = rank
      self.is_face_up = face_up
      if self.suit == "s":
         if self.rank == "A":
            image = games.load_image("as-pixilart.png")
            return image
         if self.rank == "2":
            image = games.load_image("2s-pixilart.png")
            return image
         if self.rank == "3":
            image = games.load_image("3s-pixilart.png")
            return image
         if self.rank == "4":
            image = games.load_image("4s-pixilart.png")
            return image
         if self.rank == "5":
            image = games.load_image("5s-pixilart.png")
            return image 
         if self.rank == "6":
            image = games.load_image("6s-pixilart.png")
            return image
         if self.rank == "7":
            image = games.load_image("7s-pixilart.png")
            return image
         if self.rank == "8":
            image = games.load_image("8s-pixilart.png")
            return image 
         if self.rank == "9":
            image = games.load_image("9s-pixilart.png")
            return image
         if self.rank == "10":
            image = games.load_image("10s-pixilart.png")
            return image 
         if self.rank == "J":
            image = games.load_image("js-pixilart.png")
            return image          
         if self.rank == "Q":
            image = games.load_image("qs-pixilart.png")
            return image 
         if self.rank == "K":
            image = games.load_image("Ks-pixilart.png")
            return image 
      if self.suit == "c":
         if self.rank == "A":
            image = games.load_image("ac-pixilart.png")
            return image
         if self.rank == "2":
            image = games.load_image("2c-pixilart.png")
            return image
         if self.rank == "3":
            image = games.load_image("3c-pixilart.png")
            return image
         if self.rank == "4":
            image = games.load_image("4c-pixilart.png")
            return image
         if self.rank == "5":
            image = games.load_image("5c-pixilart.png")
            return image 
         if self.rank == "6":
            image = games.load_image("6c-pixilart.png")
            return image
         if self.rank == "7":
            image = games.load_image("7c-pixilart.png")
            return image
         if self.rank == "8":
            image = games.load_image("8c-pixilart.png")
            return image 
         if self.rank == "9":
            image = games.load_image("9c-pixilart.png")
            return image
         if self.rank == "10":
            image = games.load_image("10c-pixilart.png")
            return image 
         if self.rank == "J":
            image = games.load_image("jc-pixilart.png")
            return image          
         if self.rank == "Q":
            image = games.load_image("qc-pixilart.png")
            return image 
         if self.rank == "K":
            image = games.load_image("kc-pixilart.png")
            return image
      if self.suit == "d":
         if self.rank == "A":
            image = games.load_image("ad-pixilart.png")
            return image
         if self.rank == "2":
            image = games.load_image("2d-pixilart.png")
            return image
         if self.rank == "3":
            image = games.load_image("3d-pixilart.png")
            return image
         if self.rank == "4":
            image = games.load_image("4d-pixilart.png")
            return image
         if self.rank == "5":
            image = games.load_image("5d-pixilart.png")
            return image 
         if self.rank == "6":
            image = games.load_image("6d-pixilart.png")
            return image
         if self.rank == "7":
            image = games.load_image("7d-pixilart.png")
            return image
         if self.rank == "8":
            image = games.load_image("8d-pixilart.png")
            return image 
         if self.rank == "9":
            image = games.load_image("9d-pixilart.png")
            return image
         if self.rank == "10":
            image = games.load_image("10d-pixilart.png")
            return image 
         if self.rank == "J":
            image = games.load_image("jd-pixilart.png")
            return image          
         if self.rank == "Q":
            image = games.load_image("qd-pixilart.png")
            return image 
         if self.rank == "K":
            image = games.load_image("kd-pixilart.png")
            return image
      if self.suit == "h":
         if self.rank == "A":
            image = games.load_image("ah-pixilart.png")
            return image
         if self.rank == "2":
            image = games.load_image("2h-pixilart.png")
            return image
         if self.rank == "3":
            image = games.load_image("3h-pixilart.png")
            return image
         if self.rank == "4":
            image = games.load_image("4h-pixilart.png")
            return image
         if self.rank == "5":
            image = games.load_image("5h-pixilart.png")
            return image 
         if self.rank == "6":
            image = games.load_image("6h-pixilart.png")
            return image
         if self.rank == "7":
            image = games.load_image("7h-pixilart.png")
            return image
         if self.rank == "8":
            image = games.load_image("8h-pixilart.png")
            return image 
         if self.rank == "9":
            image = games.load_image("9h-pixilart.png")
            return image
         if self.rank == "10":
            image = games.load_image("10h-pixilart.png")
            return image 
         if self.rank == "J":
            image = games.load_image("jh-pixilart.png")
            return image          
         if self.rank == "Q":
            image = games.load_image("qh-pixilart.png")
            return image 
         if self.rank == "K":
            image = games.load_image("kh-pixilart.png")
            return image  
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



if __name__ == "__main__":
   print("This is a module with classes for playing cards.")
   input("\n\nPress the enter key to exit")                                                  