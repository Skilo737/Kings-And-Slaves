import pygame
from livewires import games

games.init(screen_width = 1000, screen_height = 700, fps = 60)

class Card(games.Sprite):
   """A playing card, visually represented on the screen """
   SUITS = ["s", "c", "d", "h"]
   RANKS = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
   held = 0  
   def __init__(self, rank, suit, image, x, y, face_up = True):
      super(Card, self).__init__(image = image, x = x, y = y)
      self.suit = suit
      self.rank = rank
      self.is_face_up = face_up
      self.image = image
      self.dropped = 0
      self.pile = 0
      

   
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
   def check_card(self):
      return True
   def check_pile(self):
      return False

   def update(self):
      """ Move to mouse x position """
      if self.pile == 1:
         self.x = Pile.x
         self.y = Pile.y
      if Pointer.hold == 1 and self.held == 1:
         self.x = games.mouse.x
         self.y = games.mouse.y
      for sprite in self.overlapping_sprites:
         if sprite.check():
            if games.mouse.is_pressed(0) == False and self.held == 1: #drop
               self.held = 0
               Pointer.change_hold(0) 
               self.dropped = 1
            if games.mouse.is_pressed(0): #keep boing held
               if Pointer.hold == 1 and self.held == 1:
                  self.x = games.mouse.x
                  self.y = games.mouse.y    
               elif Pointer.hold == 0 and self.held == 0: #pick up
                  self.held = 1
                  Pointer.change_hold(1)
                  
                  self.x = games.mouse.x
                  self.y = games.mouse.y
         elif sprite.check_pile:
            hand_list[0].give(hand_list.cards[self], Pile)
            pile = 1 
               
                                      
         if self.left < 0:
            self.left = 0
         if self.right > games.screen.width:
            self.right = games.screen.width


                  
class Pointer(games.Sprite):
   """An Overwrite of the mouse"""
   image = games.load_image("3s-pixilart.png")
   hold = 0
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
   def check_card(self):
      return False
   def change_hold(inpt):
      Pointer.hold = inpt
   def check_pile(self):
      return False
   

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
      count = 0
      for suit in Card.SUITS:
         for rank in Card.RANKS:
            count += 1
            self.add(Card(rank, suit, get_card_image(rank, suit), 500 + count, 350 + count, True))
            
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
   #my_deck.shuffle()
   print("\nCompleted Shuffle\n")
   hand_list = []
   for player in range(no_players):
      hand_list.append(Hand())
   my_deck.deal(hand_list, no_cards)
   return hand_list
   # for hand in hand_list:
   #    print (hand)
   #    print ()
      
def get_card_image(rank, suit):
   print("Getting Image for", rank, suit)
   if suit == "s":
      if rank == 14:
         image = games.load_image("as-pixilart.png", transparent = False)
      elif rank == 2:
         image = games.load_image("2s-pixilart.png", transparent = False)
      elif rank == 3:
         image = games.load_image("3s-pixilart.png", transparent = False)
      elif rank == 4:
         image = games.load_image("4s-pixilart.png", transparent = False)
      elif rank == 5:
         image = games.load_image("5s-pixilart.png", transparent = False) 
      elif rank == 6:
         image = games.load_image("6s-pixilart.png", transparent = False)
      elif rank == 7:
         image = games.load_image("7s-pixilart.png", transparent = False)
      elif rank == 8:
         image = games.load_image("8s-pixilart.png", transparent = False) 
      elif rank == 9:
         image = games.load_image("9s-pixilart.png", transparent = False)
      elif rank == 10:
         image = games.load_image("10s-pixilart.png", transparent = False) 
      elif rank == 11:
         image = games.load_image("js-pixilart.png", transparent = False)          
      elif rank == 12:
         image = games.load_image("qs-pixilart.png", transparent = False) 
      elif rank == 13:
         image = games.load_image("Ks-pixilart.png", transparent = False) 
   elif suit == "c":
      if rank == 14:
         image = games.load_image("ac-pixilart.png", transparent = False)
      elif rank == 2:
         image = games.load_image("2c-pixilart.png", transparent = False)
      elif rank == 3:
         image = games.load_image("3c-pixilart.png", transparent = False)
      elif rank == 4:
         image = games.load_image("4c-pixilart.png", transparent = False)
      elif rank == 5:
         image = games.load_image("5c-pixilart.png", transparent = False)
      elif rank == 6:
         image = games.load_image("6c-pixilart.png", transparent = False)
      elif rank == 7:
         image = games.load_image("7c-pixilart.png", transparent = False)
      elif rank == 8:
         image = games.load_image("8c-pixilart.png", transparent = False)
      elif rank == 9:
         image = games.load_image("9c-pixilart.png", transparent = False)
      elif rank == 10:
         image = games.load_image("10c-pixilart.png", transparent = False)
      elif rank == 11:
         image = games.load_image("jc-pixilart.png", transparent = False)      
      elif rank == 12:
         image = games.load_image("qc-pixilart.png", transparent = False)
      elif rank == 13:
         image = games.load_image("kc-pixilart.png", transparent = False)
   elif suit == "d":
      if rank == 14:
         image = games.load_image("ad-pixilart.png", transparent = False)
      elif rank == 2:
         image = games.load_image("2d-pixilart.png", transparent = False)
      elif rank == 3:
         image = games.load_image("3d-pixilart.png", transparent = False)
      elif rank == 4:
         image = games.load_image("4d-pixilart.png", transparent = False)
      elif rank == 5:
         image = games.load_image("5d-pixilart.png", transparent = False)
      elif rank == 6:
         image = games.load_image("6d-pixilart.png", transparent = False)
      elif rank == 7:
         image = games.load_image("7d-pixilart.png", transparent = False)
      elif rank == 8:
         image = games.load_image("8d-pixilart.png", transparent = False)
      elif rank == 9:
         image = games.load_image("9d-pixilart.png", transparent = False)
      elif rank == 10:
         image = games.load_image("10d-pixilart.png", transparent = False) 
      elif rank == 11:
         image = games.load_image("jd-pixilart.png", transparent = False)          
      elif rank == 12:
         image = games.load_image("qd-pixilart.png", transparent = False) 
      elif rank == 13:
         image = games.load_image("kd-pixilart.png", transparent = False)
   elif suit == "h":
      if rank == 14:
         image = games.load_image("ah-pixilart.png", transparent = False)
      elif rank == 2:
         image = games.load_image("2h-pixilart.png", transparent = False)
      elif rank == 3:
         image = games.load_image("3h-pixilart.png", transparent = False)
      elif rank == 4:
         image = games.load_image("4h-pixilart.png", transparent = False)
      elif rank == 5:
         image = games.load_image("5h-pixilart.png", transparent = False) 
      elif rank == 6:
         image = games.load_image("6h-pixilart.png", transparent = False)
      elif rank == 7:
         image = games.load_image("7h-pixilart.png", transparent = False)
      elif rank == 8:
         image = games.load_image("8h-pixilart.png", transparent = False) 
      elif rank == 9 :
         image = games.load_image("9h-pixilart.png", transparent = False)
      elif rank == 10:
         image = games.load_image("10h-pixilart.png", transparent = False) 
      elif rank == 11:
         image = games.load_image("jh-pixilart.png", transparent = False)          
      elif rank == 12:
         image = games.load_image("qh-pixilart.png", transparent = False) 
      elif rank == 13:
         image = games.load_image("kh-pixilart.png", transparent = False)
   
   image = pygame.transform.scale(image, (40, 60))
   print("Returning image")      
   return image
   
class Pile(games.Sprite):
  image = games.load_image("pile.png")
  pile_cards = []
  overlap = 0
    
  def __init__(self, x = 500, y = 350):
    """ initialize a pizza object """
    super(Pile, self).__init__(image = games.load_image("pile.png", transparent = False), x = games.screen.width//2, y = games.screen.height//2)
    
  def determine_value(self):
    try:
      len(pile_cards) == 0
    except:
      self.value = self.pile_cards[len(self.pile_cards)].rank
      return self.value
    else:          
      self.value = 0
      return self.value
   
  def update(self):
     turn = 0
     print(turn)
     print(self.pile_cards)
     if turn == 3:
        turn = 0
        current_hand = hand_list[0 + turn]
        high_cards = []
     if turn != 0:
         for i in current_hand.cards:
           if i.rank > Pile.determine_value:
             high_cards.append(i)
             high_cards.sort()
             current_hand.give(high_cards[0], Pile)
           elif turn == 0:
             while Pile.placed != 1:
               pass
             turn += 1
  def placed(self):
    for card in self.overlapping_sprites:
      if card.check:
        if overlap == 0:
            self.overlap = 1
        if overlap == 1:
            self.overlap = 0
            return 1
  def check(self):
   return False
  def check_card(self):
   return False
  def check_pile(self):
   return True
    
     
      

def main():
   wall_image = games.load_image(("Cardsbackdrop.jpg"), transparent = False)
   games.screen.background = wall_image
   
   hand_list = setup()
   global hand_list
   
    

   games.screen.event_grab = True
   games.mouse.is_visible = False
   the_pile = Pile()
   games.screen.add(Pile())
   
   x = 10
   y = 20
   for hand in hand_list:
       for card in hand.cards:
          cardimage = get_card_image(card.rank, card.suit)                       
          cardsprite = Card(card.rank, card.suit, cardimage, x, y, False)                        
          games.screen.add(cardsprite)
          x += 30
       x = 10
       y += 30
   
   hand = hand_list[0]
   for card in hand.cards:
      cardimage = get_card_image(card.rank, card.suit)                       
      cardsprite = Card(card.rank, card.suit, cardimage, x, y, False)                        
      games.screen.add(cardsprite)
      x += 30
   
   mouse = Pointer(image = games.load_image("cursor.png", transparent = True), x = games.mouse.x, y = games.mouse.y)

   games.screen.add(mouse)
   
   print(Pile.pile_cards)
   games.screen.mainloop()


main()
