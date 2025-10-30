def ask_player_action() -> str:
    while True:
        player_input = input("enter your choice")
        if player_input == "S":
            print("ok its dealer turn")
            break
        if player_input == "H":
            print("ok there is another card")
            break
        else:
            print("invalid input")
            break
    return player_input