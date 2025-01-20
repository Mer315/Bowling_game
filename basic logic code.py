def winner(player1, player2):
    def calculate_score(player):
        n = len(player)                       
        score = 0
        prev1 = 0
        prev2 = 0
        
        for i in range(n):
            present_turn = player[i]
            if prev1 == 10 or prev2 == 10:
                turn_score = 2 * present_turn
            else:
                turn_score = present_turn
            
            score += turn_score
            print(f"Turn {i+1}: Current turn pins = {present_turn}, "
                  f"Previous two turns = ({prev2}, {prev1}), "
                  f"Turn score = {turn_score}, Total score = {score}")
            
            prev2 = prev1
            prev1 = present_turn
        
        return score
    
    print("Player 1:")
    score1 = calculate_score(player1)
    print("\nPlayer 2:")
    score2 = calculate_score(player2)
    
    print(f"\nFinal Score - Player 1: {score1}, Player 2: {score2}")
    
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0

def get_player_input(player_num, n):
    while True:
        try:
            player_input = input(f"Enter {n} scores for Player {player_num} (comma-separated and each between 0 and 10): ")
            player_scores = [int(x) for x in player_input.split(',')]
            if len(player_scores) == n and all(0 <= score <= 10 for score in player_scores):
                return player_scores
            else:
                print(f"Enter exactly {n} scores, each between 0 and 10. Try again.")
        except ValueError:
            print("Invalid input. Enter integers separated by commas.")

# Get input for n
while True:
    try:
        n = int(input("Enter the number of turns (n): "))
        if n > 0:
            break
        else:
            print("The number of turns must be a positive integer. Please try again.")
    except ValueError:
        print("Invalid input.Enter a positive integer.")

# Get inputs for both players
player1 = get_player_input(1, n)
player2 = get_player_input(2, n)

# Determine the winner
result = winner(player1, player2)
print(f"Result: {result}")