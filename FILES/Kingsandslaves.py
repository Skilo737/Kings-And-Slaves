import pygame
from livewires import games

games.init(screen_width = 1000, screen_height = 700, fps = 60)

class Card(games.Sprite):
   """A playing card, visually represented on the screen """
   SUITS = ["s", "c", "d", "h"]
   RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]   
   def __init__(self, rank, suit, image, x, y, face_up = True):
      super(Card, self).__init__(image = image, x = x, y = y)
      self.suit = suit
      self.rank = rank
      self.is_face_up = face_up
      self.image = image
      

   
   def flip(self, flip_up):
      if flip_up == False:
         print("flipping to back")
         super(Card, self).__init__(image = games.load_image("card-backside.png"), x = games.screen.width//2, y = games.screen.height//2)
      else:
         print("Flipping to Front")
         super(Card, self).__init__(image = self.image, x = games.screen.width//2, y = games.screen.height//2)
      self.is_face_up = not self.is_face_up
   def check(self):
      return False


   def update(self):
      """ Move to mouse x position """
      for Pointer in self.overlapping_sprites:
         if Pointer.check():
            if games.mouse.is_pressed(0):
               self.x = games.mouse.x
               self.y = games.mouse.y            
        
         if self.left < 0:
            self.left = 0
         if self.right > games.screen.width:
            self.right = games.screen.width

                  
class Pointer(games.Sprite):
   """An Overwrite of the mouse"""
   image = games.load_image("3s-pixilart.png")
   def __init__(self, image, x = 0, y = 0):
      super(Pointer, self).__init__(image = image, x = x, y = y)
   def update(self):
      self.x = games.mouse.x
      self.y = games.mouse.y
      
      if self.left < 0:
            self.left = 0
      if self.right > games.screen.width:
            self.right = games.screen.width
   def check(self):
      return True
   

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
            self.add(Card(rank, suit, get_card_image(rank, suit), 500, 350, True))
            
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
               print("Can't continue to deal. Out of cards.\n")




def setup():
   no_players = 4
   no_cards = 13
   
   my_deck = Deck()
   my_deck.populate()
   print("\nCompleted Population")
   my_deck.shuffle()
   print("\nCompleted Shuffle\n")
   hand_list = []
   for player in range(no_players):
      hand_list.append(Hand())
   my_deck.deal(hand_list, no_cards)
   
   # for hand in hand_list:
   #    print (hand)
   #    print ()
      
def get_card_image(rank, suit):
   print("Getting Image for", rank, suit)
   if suit == "s":
      if rank == "A":
         image = games.load_image("as-pixilart.png", transparent = False)
      elif rank == "2":
         image = games.load_image("2s-pixilart.png", transparent = False)
      elif rank == "3":
         image = games.load_image("3s-pixilart.png", transparent = False)
      elif rank == "4":
         image = games.load_image("4s-pixilart.png", transparent = False)
      elif rank == "5":
         image = games.load_image("5s-pixilart.png", transparent = False) 
      elif rank == "6":
         image = games.load_image("6s-pixilart.png", transparent = False)
      elif rank == "7":
         image = games.load_image("7s-pixilart.png", transparent = False)
      elif rank == "8":
         image = games.load_image("8s-pixilart.png", transparent = False) 
      elif rank == "9":
         image = games.load_image("9s-pixilart.png", transparent = False)
      elif rank == "10":
         image = games.load_image("10s-pixilart.png", transparent = False) 
      elif rank == "J":
         image = games.load_image("js-pixilart.png", transparent = False)          
      elif rank == "Q":
         image = games.load_image("qs-pixilart.png", transparent = False) 
      elif rank == "K":
         image = games.load_image("Ks-pixilart.png", transparent = False) 
   elif suit == "c":
      if rank == "A":
         image = games.load_image("ac-pixilart.png", transparent = False)
      elif rank == "2":
         image = games.load_image("2c-pixilart.png", transparent = False)
      elif rank == "3":
         image = games.load_image("3c-pixilart.png", transparent = False)
      elif rank == "4":
         image = games.load_image("4c-pixilart.png", transparent = False)
      elif rank == "5":
         image = games.load_image("5c-pixilart.png", transparent = False)
      elif rank == "6":
         image = games.load_image("6c-pixilart.png", transparent = False)
      elif rank == "7":
         image = games.load_image("7c-pixilart.png", transparent = False)
      elif rank == "8":
         image = games.load_image("8c-pixilart.png", transparent = False)
      elif rank == "9":
         image = games.load_image("9c-pixilart.png", transparent = False)
      elif rank == "10":
         image = games.load_image("10c-pixilart.png", transparent = False)
      elif rank == "J":
         image = games.load_image("jc-pixilart.png", transparent = False)      
      elif rank == "Q":
         image = games.load_image("qc-pixilart.png", transparent = False)
      elif rank == "K":
         image = games.load_image("kc-pixilart.png", transparent = False)
   elif suit == "d":
      if rank == "A":
         image = games.load_image("ad-pixilart.png", transparent = False)
      elif rank == "2":
         image = games.load_image("2d-pixilart.png", transparent = False)
      elif rank == "3":
         image = games.load_image("3d-pixilart.png", transparent = False)
      elif rank == "4":
         image = games.load_image("4d-pixilart.png", transparent = False)
      elif rank == "5":
         image = games.load_image("5d-pixilart.png", transparent = False)
      elif rank == "6":
         image = games.load_image("6d-pixilart.png", transparent = False)
      elif rank == "7":
         image = games.load_image("7d-pixilart.png", transparent = False)
      elif rank == "8":
         image = games.load_image("8d-pixilart.png", transparent = False)
      elif rank == "9":
         image = games.load_image("9d-pixilart.png", transparent = False)
      elif rank == "10":
         image = games.load_image("10d-pixilart.png", transparent = False) 
      elif rank == "J":
         image = games.load_image("jd-pixilart.png", transparent = False)          
      elif rank == "Q":
         image = games.load_image("qd-pixilart.png", transparent = False) 
      elif rank == "K":
         image = games.load_image("kd-pixilart.png", transparent = False)
   elif suit == "h":
      if rank == "A":
         image = games.load_image("ah-pixilart.png", transparent = False)
      elif rank == "2":
         image = games.load_image("2h-pixilart.png", transparent = False)
      elif rank == "3":
         image = games.load_image("3h-pixilart.png", transparent = False)
      elif rank == "4":
         image = games.load_image("4h-pixilart.png", transparent = False)
      elif rank == "5":
         image = games.load_image("5h-pixilart.png", transparent = False) 
      elif rank == "6":
         image = games.load_image("6h-pixilart.png", transparent = False)
      elif rank == "7":
         image = games.load_image("7h-pixilart.png", transparent = False)
      elif rank == "8":
         image = games.load_image("8h-pixilart.png", transparent = False) 
      elif rank == "9":
         image = games.load_image("9h-pixilart.png", transparent = False)
      elif rank == "10":
         image = games.load_image("10h-pixilart.png", transparent = False) 
      elif rank == "J":
         image = games.load_image("jh-pixilart.png", transparent = False)          
      elif rank == "Q":
         image = games.load_image("qh-pixilart.png", transparent = False) 
      elif rank == "K":
         image = games.load_image("kh-pixilart.png", transparent = False)
   print("Returning image")      
   return image

def main():
   wall_image = games.load_image(("Cardsbackdrop.jpg"), transparent = False)
   games.screen.background = wall_image
   
   setup()
   
   mouse = Pointer(image = games.load_image("3s-pixilart.png"), x = games.mouse.x, y = games.mouse.y)
   games.screen.add(mouse)
    

   ###### Im Testing stuff DO NOT USE IN FINISHED GAME########### 
   cardimage = get_card_image("K", "d")                       
   cardsprite = Card("K", "d", cardimage, 600, 250, False)                        
   games.screen.add(cardsprite)                  
   ##############################################################
   games.screen.event_grab = True
   games.mouse.is_visible = False
   games.screen.mainloop()


main()