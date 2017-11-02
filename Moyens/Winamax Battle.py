from collections import deque
from re import sub
from sys import stderr

p1 = deque([], maxlen = 52)
p2 = deque([], maxlen = 52)

n = int(input())  # the number of cards for player 1
for i in range(n):
    p1.append(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    p2.append(input())    # the m cards of player 2

# Sorted from lowest rank to highest.
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Decks only when case of war.
p1_war = []
p2_war = []

rounds = 0

try:
    while p1 and p2:
    
        rounds += 1
    
        c1 = p1.popleft()
        v1 = sub('[DCHS]', '', c1)
        print('Card for P1: {}'.format(c1), file = stderr)
    
        c2 = p2.popleft()
        v2 = sub('[DCHS]', '', c2)
        print('Card for P2: {}'.format(c2), file = stderr)
    
        # Order is : P1 cards always first, then P2 cards.
        result = [card for card in p1_war] + [c1] + [card for card in p2_war] + [c2]
        print('The card that will be won: {}'.format(result), file = stderr)
    
        if ranks.index(v1) > ranks.index(v2):
            print('P1 won this turn.', file = stderr)
            p1.extend(result)

            p1_war, p2_war, result = [], [], []
    
        elif ranks.index(v1) < ranks.index(v2):
            print('P2 won this turn.', file = stderr)
            p2.extend(result)
            
            p1_war, p2_war, result = [], [], []
    
        else:
            print('WAR !', file = stderr)
    
            # Exception to short-circuit the flow.
            if len(p1) <= 3 or len(p2) <= 3:
                raise ValueError
    
            p1_war.append(c1)
            p2_war.append(c2)
    
            for x in range(3):
                p1_war.append(p1.popleft())
                p2_war.append(p2.popleft())
                
            rounds -= 1
         
        print('At end of turn {} for P1: {}'.format(rounds, p1), file = stderr)
        print('At end of turn {} for P2: {}\n'.format(rounds, p2), file = stderr)
        
    if p1:
        print('1 {}'.format(rounds))
    else:
        print('2 {}'.format(rounds))

except ValueError:
    print('PAT')
