import os
data_folder = os.path.dirname(__file__) + '/'
file_name = '2.txt'

f = open(data_folder + file_name)

options = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def calculate_score(opp_move, me_move):
    score = 0
    opp = options.get(opp_move)
    me = options.get(me_move)

    if me == 3:
        if opp == 2:
            score += 6
        elif opp == me:
            score += 3
    elif me == 2:
        if opp == 1:
            score += 6
        elif opp == me:
            score += 3
    elif me == 1:
        if opp == 3:
            score += 6
        elif opp == me:
            score += 3
    
    score += me
    return score

total_score = 0

for line in f:
    moves = line.replace('\n','').split(' ')
    total_score += calculate_score(moves[0], moves[1])

print(total_score)

f.close()