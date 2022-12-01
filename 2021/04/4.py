# 04
import numpy as np
import copy

lines = open("input.txt", 'r').read().splitlines()

# First line is order of drawings
drawings = lines[0].split(',')


# then boards
boards = []
marked = [] 
cur = np.zeros((5,5))
lin_num = 0
for line in lines[2:]:
    if len(line) < 1:    
        continue
    
    cur[lin_num] = np.fromstring(line, dtype=np.int8, sep=' ')
    
    lin_num += 1
    if lin_num >= 5:
        boards.append(cur)
        cur = np.zeros((5,5))
        lin_num = 0
        marked.append(np.zeros(shape=(5,5),dtype=np.int8))

# mark board
def mark_board(boards, marked, b, val):
    for i in range(5):
        for j in range(5):
            if boards[b][i][j] == val:
                marked[b][i][j] = 1
                return #only 1 per board

def mark_boards(boards, marked, val):
    for b in range(len(boards)):
        mark_board(boards, marked, b, val)

def check_board(marked, b):
    for i in range(5):
        hor, vert = True, True
        for j in range(5):
            if not marked[b][i][j]:
                hor = False
            if not marked[b][j][i]:
                vert = False
        if hor or vert:
            return True
    return False


#check boards
def check_boards(boards, marked ):
    winners = []
    for b in range(len(boards)):
        if check_board(marked,b):
            winners.append(b)
    if len(winners) > 0:
        return winners
    else:
        return None
            

# score is computed from sum of unmarked * value just called
all_draws = []
winners = None

for draw in drawings:
    d = int(draw)
    all_draws.append(d)
    mark_boards(boards, marked, d)
    winners = check_boards(boards, marked)
    if winners:
        break

winner = winners[0]
print('Part 1:')
print("Winning board: #", winner)
print("Board = \n", boards[winner])
print(" Marked =\n", marked[winner])
print(" Draws = ", all_draws)

# Scoring
mul = np.subtract(1, marked[winner])
unmarked = np.multiply(boards[winner],mul)
score = np.sum(unmarked) * all_draws[-1]
print()
print("  Score =", score)
# 1564260 is too high


losing_boards = copy.deepcopy(boards)
# all_draws = []
# del losing_boards[winner]
# del marked[winner]
# last_draw = drawings.index(str(all_draws[-1]))
stop = False
for draw in drawings:
    d = int(draw)
    all_draws.append(d)
    mark_boards(losing_boards, marked, d)
    winners = check_boards(losing_boards, marked)
    if winners:
        for w in winners[::-1]:
            if len(losing_boards) == 1:
                stop= True
                break
            losing_boards.pop(w)  
            marked.pop(w)  
        if stop:
            break
# loser = boards[0]
loser = -1
for b in range(len(boards)):
    if np.sum(np.abs(np.subtract(boards[b], losing_boards[0]))) < 0.01:
        loser = b

print('Part 2:')
print("Losing board: #", loser)
print("Board = \n", losing_boards[0])
print(" Marked = \n", marked[0])
print(" Draws = ", all_draws)

# Scoring
mul = np.subtract(1, marked[0])
unmarked = np.multiply(losing_boards[0],mul)
score = np.sum(unmarked) * all_draws[-1]
print()

# print(unmarked)
# print(all_draws[-1])
print("  Losing Score =", score)

print("Done")
# 7434 is too low

