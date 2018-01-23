from sys import stderr
from typing import List, Tuple


def marvin_in_good_direction(elevator_pos: int, clone_pos: int, direction: str) -> bool:
    """
    Is the clone going in the good direction?

    Args:
        elevator_pos (int) - The position of the elevator.
        clone_pos (int) - The position of Marvin's clone.
        direction (str) - RIGHT or LEFT.
    """
    if elevator_pos >= clone_pos and direction == 'RIGHT':
        return True
    elif elevator_pos <= clone_pos and direction == 'LEFT':
        return True
    else:
        return False


nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

# To store all elevators flort and position.
elevators_info: List[Tuple[int, int]] = []
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators_info.append((elevator_floor, elevator_pos))


while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    
    elevator_pos: int = 0
    try:
        elevator_pos = next(info[1] for info in elevators_info if info[0] == clone_floor)
    except StopIteration:
        elevator_pos = exit_pos
    
    if marvin_in_good_direction(elevator_pos, clone_pos, direction):
        print('WAIT')
    else:
        print('BLOCK')
