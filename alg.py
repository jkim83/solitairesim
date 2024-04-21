import solitaire

def simulate_game(board, steps=[], dead_ends=0, moves_made=0, consecutive_draws=0):
    print("Top card of waste:", board.piles[12][1] if board.piles[12] else "Empty")
    moveMade = False

    # RULE 1: Move to pile.
    for i in range(8):  # 
        for j in range(8, 12):  # Check if any card can be moved from tableau to pile
            if board.check_validity(i, j):
                board.move(i, j)
                print(i, j)
                moveMade = True
                return
    
    # RULE 2: Move between tableaus.
    # note: remember previous btwn tableaus so you don't have infinite loop?
    if not moveMade:
        for i in range(8):  # Check if ANY movement within tableaus is valid
            for j in range(8):  # Check if any card can be moved within the tableau
                if board.check_validity(i, j):
                    board.move(i, j)
                    print(i, j)
                    moveMade = True
                    return

    # RULE 3: Move from waste to tableaus.
    if not moveMade and board.piles[12]:  # Check if no move has been made and there are cards in the waste pile
        for i in range(8):  # Iterate over tableaus
            if board.check_validity(12, i):  # Check if moving from waste to tableau 'i' is valid
                board.move(12, i)  # Move the card from waste to tableau 'i'
                print('RULE #3')
                print(12, i)
                moveMade = True
                return

    # RULE 4: Hit hand if no move has been made.
    if not moveMade:
        board.hitHand()
        print("Hand hit")
    
    return

def main():
    board = solitaire.Solitaire()

    board.displayBoard()

    for _ in range(20):
        simulate_game(board)
        board.displayBoard()

if __name__ == "__main__":
    main()
