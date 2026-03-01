def simulate_game(player_a, player_b):

    deck_a = list(player_a)
    deck_b = list(player_b)
    pile = []

    turn = "A"
    penalty = 0
    penalty_owner = None

    cards_played = 0
    tricks = 0

    face = {"J": 1, "Q": 2, "K": 3, "A": 4}

    def normalize(deck):
        return "".join(c if c in face else "N" for c in deck)

    history = set()
    history.add((normalize(deck_a), normalize(deck_b), turn))

    while True:

        active = deck_a if turn == "A" else deck_b
        other = deck_b if turn == "A" else deck_a

    
        if not active:
            if pile:
                other.extend(pile)
                tricks += 1
            return {"status": "finished", "cards": cards_played, "tricks": tricks}

        card = active.pop(0)
        pile.append(card)
        cards_played += 1

        if card in face:
            penalty = face[card]
            penalty_owner = turn
            turn = "B" if turn == "A" else "A"

        else:
            if penalty > 0:
                penalty -= 1

                if penalty == 0:
                    winner = deck_a if penalty_owner == "A" else deck_b
                    winner.extend(pile)
                    pile.clear()
                    tricks += 1

                    turn = penalty_owner
                    penalty_owner = None

                    
                    if not deck_a or not deck_b:
                        return {"status": "finished", "cards": cards_played, "tricks": tricks}

                   
                    state = (normalize(deck_a), normalize(deck_b), turn)
                    if state in history:
                        return {"status": "loop", "cards": cards_played, "tricks": tricks}
                    history.add(state)

            else:
                turn = "B" if turn == "A" else "A"

  


 

