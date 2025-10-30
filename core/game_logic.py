from core.deck import *
def calculate_hand_value(hand: list[dict]) -> int:
    value = 0
    for i in hand:
        value +=i ["value"]
    return value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None :
       new_deck = deck
       player_hand = player
       dealer_hand = dealer
       player_hand["value"] = 0
       dealer_hand["value"] = 0
       for i in range(2):
           card = [new_deck.pop(0)]
           card_value = calculate_hand_value(card)
           player_hand["value"]+=card_value
       for i in range(2):
           card = [new_deck.pop(0)]
           card_value = calculate_hand_value(card)
           dealer_hand["value"]+=card_value
       print(f'dealer hand = {dealer_hand["value"]}, player hand = {player_hand["value"]}')





def dealer_play(deck: list[dict], dealer: dict) -> bool:
    new_deck = deck
    value = dealer["value"]
    card = new_deck.pop(0)
    value += card["value"]
    while value <= 17:
        card = new_deck.pop(0)
        card_value = calculate_hand_value([card])
        value += card_value
    print(value)
    if value > 21:
        return False
    if 17 <= value and value<= 21:
        return True




