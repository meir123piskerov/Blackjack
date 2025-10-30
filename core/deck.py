import random
def build_standard_deck() -> list[dict]:

    list_of_cards = [ "A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    suite_of_cards = ["H", "C", "D", "S"]

    a = {}

    deck_of_cards = []
    value = 1

    for suite in suite_of_cards:
        for rank in list_of_cards:
            a["rank"] = rank
            a["suite"] = suite
            if value != 11 and value != 12 and value != 13:
                a["value"] = value
            else:
                a["value"] = 10
            deck_of_cards.append(a)
            a = {}
            value += 1
        value = 1
    return deck_of_cards





def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    count = 0
    while count <= swaps:
        i = random.randrange(0,len(deck))
        j = random.randrange(0,len(deck))
        if i != j:
            if deck[i]["suite"] == "H":
                if j % 5 == 0:
                    deck[i],deck[j] = deck[j],deck[i]

                    count +=1
                else:
                    continue
            if deck[i]["suite"] == "C":
                if j % 3 == 0:
                    deck[i],deck[j] = deck[j],deck[i]
                    count +=1
                else:
                    continue
            if deck[i]["suite"] == "D":
                if j % 2 == 0:
                    deck[i],deck[j] = deck[j],deck[i]
                    count +=1
                else:
                    continue
            if deck[i]["suite"] == "S":
                if j % 7 == 0:
                    deck[i],deck[j] = deck[j],deck[i]
                    count +=1
                else:
                    continue
            else:
                continue
    return deck
