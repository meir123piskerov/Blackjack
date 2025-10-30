from core.deck import *
from core.player_io import *
from core.game_logic import *

player = {}
dealer = {}

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    new_deck = deck
    player_hand = player
    dealer_hand = dealer
    deal_two_each(new_deck,player,dealer_hand)
    while True:
        player_choice = ask_player_action()
        if player_choice == "H":
            card = new_deck.pop(0)
            card_value = calculate_hand_value([card])
            player_hand["value"] += card_value
            print(f'now player value is {player_hand["value"]}')
            if player_hand["value"] > 21:
                print("you lost , you pass 21")
                break
            else:
                 continue
        elif player_hand == "S":
            dealer_play(new_deck, dealer_hand)
            print()
        break
    if dealer_hand["value"] > player_hand["value"]:
        print("dealer won")
    elif player_hand["value"]>dealer_hand["value"]:
        if player_hand["value"] <= 21:
            print("player won")
    elif player_hand["value"] == dealer_hand["value"]:
        print("its a draw")

if __name__ == "__main__":
    run_full_game(shuffle_by_suit(build_standard_deck()),player,dealer)








