from sys import stderr
from typing import Dict, List, Tuple

n = int(input())
m = int(input())

total_yes: int = 0
total_no: int = 0

voters: Dict[str, int] = dict()

for i in range(n):
    person_name, nb_vote = input().split()
    nb_vote = int(nb_vote)
    voters[person_name] = nb_vote
    
# Storage of how voted what. First tuple value is YES, second is NO.
infos: Dict[str, List[int]] = dict()
voted: Dict[str, int] = dict()

for i in range(m):
    voter_name, vote_value = input().split()
    invalid: bool = False
    
    if voter_name not in voters:
        #print(f'{voter_name} is trying to vote but he is not allowed.', file = stderr)
        continue
    
    if vote_value.lower() not in ['yes', 'no']:
        print(f'{voter_name} voted something invalid (voted "{vote_value}").', file = stderr)
        invalid = True
    
    yes: int = 1 if vote_value.lower() == 'yes' else 0
    no: int = 1 if vote_value.lower() == 'no' else 0
    
    #print(f'Now it is {voter_name}', file = stderr)
    #print(f'{voter_name} voted {vote_value}.', file = stderr)
    #print(f'Yes value: {yes} No value: {no}', file = stderr)
    
    if voter_name not in infos:
        #print(f'{voter_name} was added in list of voters.', file = stderr)
        infos[voter_name] = [yes, no]
        voted[voter_name] = 1
        
        total_yes += yes
        total_no += no
        
    else:
        voted[voter_name] += 1
        
        # That person voted too much.
        if voted[voter_name] > voters[voter_name]:
            #print(f'{voter_name} voted too much times ({infos[voter_name][0] + infos[voter_name][1]} times). Everything becomes invalid.', file = stderr)
            invalid = True
        
        if not invalid:
            infos[voter_name][0] += yes
            infos[voter_name][1] += no
            
            total_yes += yes
            total_no += no
            
        else:
            # We want to substract only once.
            if voters[voter_name] != -1:
                total_yes -= infos[voter_name][0]
                total_no -= infos[voter_name][1]
                voters[voter_name] = -1

print(f'{total_yes} {total_no}')
