from superwires import games
import Cards


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
   games.init(screen_width = 640, screen_height = 480, fps = 60)
   wall_image = games.load_image("(background)", transparent = False)
   games.screen.background = wall_image

main()