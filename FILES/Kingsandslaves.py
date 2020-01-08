import pygame
from livewires import games
import Cards

games.init(screen_width = 640, screen_height = 480, fps = 60)

def setup():
   no_players = 4
   no_cards = 13
   
   my_deck = Cards.Deck()
   my_deck.populate()
   my_deck.shuffle()
   hand_list = []
   for player in range(no_players):
      hand_list.append(Cards.Hand())
   my_deck.deal(hand_list, no_cards)
   
   for hand in hand_list:
      print (hand)
      print ()
   

def main():
   wall_image = games.load_image(("Cardsbackdrop.jpg"), transparent = False)
   games.screen.background = wall_image
   
   setup()
    
   card = Cards.Card("A", "c")
   games.screen.add(card)
   
 
   
   games.screen.mainloop()


main()