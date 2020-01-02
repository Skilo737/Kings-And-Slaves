#Treely Dowd - 12/9/19

# Cards Module
# Basic classes for a game with playing cards

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



if __name__ == "__main__":
   print("This is a module with classes for playing cards.")
   input("\n\nPress the enter key to exit")                                                  