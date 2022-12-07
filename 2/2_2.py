import os
data_folder = os.path.dirname(__file__) + '/'
file_name = '2.txt'

f = open(data_folder + file_name)

options = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6
}

def calculate_score(opp_move, outcome):
    score = 0
    opp = options.get(opp_move)
    outcome_score = options.get(outcome)

    if outcome_score == 6:
        if opp == 1 or opp == 2:
            score += opp + 1
        elif opp == 3:
            score += 1
    elif outcome_score == 3:
        score += opp
    elif outcome_score == 0:
        if opp == 3 or opp == 2:
            score += opp - 1
        elif opp == 1:
            score += 3
    
    score += outcome_score
    return score

total_score = 0

for line in f:
    moves = line.replace('\n','').split(' ')
    total_score += calculate_score(moves[0], moves[1])

print(total_score)

f.close()