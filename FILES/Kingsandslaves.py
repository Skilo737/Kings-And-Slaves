import pygame
from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 60)

class Card(games.Sprite):
   """A playing card. """
   SUITS = ["s", "c", "d", "h"]
   RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]   
   def __init__(self, rank, suit, image, face_up = True):
      super(Card, self).__init__(image = image, x = games.screen.width//2, y = games.screen.height//2)
      self.suit = suit
      self.rank = rank
      self.is_face_up = face_up

   
   def flip(self):
      if self.is_face_up:
         super(Card, self).__init__(image = games.load_image("card-backside.png"), x = games.screen.width//2, y = games.screen.height//2)
      else:
         super(Card, self).__init__(image = self.image, x = games.screen.width//2, y = games.screen.height//2)
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
      
def get_card_image(rank, suit):
   if suit == "s":
      if rank == "A":
         image = games.load_image("as-pixilart.png")
      elif rank == "2":
         image = games.load_image("2s-pixilart.png")
      elif rank == "3":
         image = games.load_image("3s-pixilart.png")
      elif rank == "4":
         image = games.load_image("4s-pixilart.png")
      elif rank == "5":
         image = games.load_image("5s-pixilart.png") 
      elif rank == "6":
         image = games.load_image("6s-pixilart.png")
      elif rank == "7":
         image = games.load_image("7s-pixilart.png")
      elif rank == "8":
         image = games.load_image("8s-pixilart.png") 
      elif rank == "9":
         image = games.load_image("9s-pixilart.png")
      elif rank == "10":
         image = games.load_image("10s-pixilart.png") 
      elif rank == "J":
         image = games.load_image("js-pixilart.png")          
      elif rank == "Q":
         image = games.load_image("qs-pixilart.png") 
      elif rank == "K":
         image = games.load_image("Ks-pixilart.png") 
   elif suit == "c":
      if rank == "A":
         image = games.load_image("ac-pixilart.png")
      elif rank == "2":
         image = games.load_image("2c-pixilart.png")
      elif rank == "3":
         image = games.load_image("3c-pixilart.png")
      elif rank == "4":
         image = games.load_image("4c-pixilart.png")
      elif rank == "5":
         image = games.load_image("5c-pixilart.png")
      elif rank == "6":
         image = games.load_image("6c-pixilart.png")
      elif rank == "7":
         image = games.load_image("7c-pixilart.png")
      elif rank == "8":
         image = games.load_image("8c-pixilart.png")
      elif rank == "9":
         image = games.load_image("9c-pixilart.png")
      elif rank == "10":
         image = games.load_image("10c-pixilart.png")
      elif rank == "10":
         image = games.load_image("jc-pixilart.png")      
      elif rank == "Q":
         image = games.load_image("qc-pixilart.png")
      elif rank == "K":
         image = games.load_image("kc-pixilart.png")
   elif suit == "d":
      if rank == "A":
         image = games.load_image("ad-pixilart.png")
      elif rank == "2":
         image = games.load_image("2d-pixilart.png")
      elif rank == "3":
         image = games.load_image("3d-pixilart.png")
      elif rank == "4":
         image = games.load_image("4d-pixilart.png")
      elif rank == "5":
         image = games.load_image("5d-pixilart.png")
      elif rank == "6":
         image = games.load_image("6d-pixilart.png")
      elif rank == "7":
         image = games.load_image("7d-pixilart.png")
      elif rank == "8":
         image = games.load_image("8d-pixilart.png")
      elif rank == "9":
         image = games.load_image("9d-pixilart.png")
      elif rank == "10":
         image = games.load_image("10d-pixilart.png") 
      elif rank == "J":
         image = games.load_image("jd-pixilart.png")          
      elif rank == "Q":
         image = games.load_image("qd-pixilart.png") 
      elif rank == "K":
         image = games.load_image("kd-pixilart.png")
   elif suit == "h":
      if rank == "A":
         image = games.load_image("ah-pixilart.png")
      elif rank == "2":
         image = games.load_image("2h-pixilart.png")
      elif rank == "3":
         image = games.load_image("3h-pixilart.png")
      elif rank == "4":
         image = games.load_image("4h-pixilart.png")
      elif rank == "5":
         image = games.load_image("5h-pixilart.png") 
      elif rank == "6":
         image = games.load_image("6h-pixilart.png")
      elif rank == "7":
         image = games.load_image("7h-pixilart.png")
      elif rank == "8":
         image = games.load_image("8h-pixilart.png") 
      elif rank == "9":
         image = games.load_image("9h-pixilart.png")
      elif rank == "10":
         image = games.load_image("10h-pixilart.png") 
      elif rank == "J":
         image = games.load_image("jh-pixilart.png")          
      elif rank == "Q":
         image = games.load_image("qh-pixilart.png") 
      elif rank == "K":
         image = games.load_image("kh-pixilart.png")
   return image

def main():
   wall_image = games.load_image(("Cardsbackdrop.jpg"), transparent = False)
   games.screen.background = wall_image
   
    
   cardimage = get_card_image("6", "s")
   cardsprite = Card("A", "s", cardimage)
   games.screen.add(cardsprite)
 
   games.screen.mainloop()


main()