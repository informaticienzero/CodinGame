from sys import stderr
from typing import List


class Registers:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
        
    def to_int(self, value: str) -> int:
        result: int = 0
        try:
            result = int(value)
        except:
            result = self.register_value(value)
        return result

        
    def register_value(self, register: str) -> int:
        if register == 'a':
            return self.a
        elif register == 'b':
            return self.b
        elif register == 'c':
            return self.c
        elif register == 'd':
            return self.d
        
        
    def update(self, register: str, value: str) -> None:
        value_received: int = self.to_int(value)
        
        if register == 'a':
            self.a = value_received
        elif register == 'b':
            self.b = value_received
        elif register == 'c':
            self.c = value_received
        else:
            self.d = value_received
            
    
    def change(self, register: str, values: List[str], op: str) -> None:
        current_register_value: int = self.register_value(register)
        
        value_1: int = self.to_int(values[0])
        value_2: int = self.to_int(values[1])
        
        if op == '+':
            self.update(register, str(value_1 + value_2))
        elif op == '-':
            self.update(register, str(value_1 - value_2))


a, b, c, d = [int(i) for i in input().split()]
registers: Registers = Registers(a, b, c, d)
n = int(input())

instructions: List[str] = []
for i in range(n):
    instructions.append(input())

index: int = 0
next_instruction: str = instructions[index]

while next_instruction != '':
    instruction: List[str] = next_instruction.split()
    
    if instruction[0] == 'MOV':
        registers.update(instruction[1], instruction[2])
    elif instruction[0] == 'ADD':
        registers.change(instruction[1], [instruction[2], instruction[3]], '+')
    elif instruction[0] == 'SUB':
        registers.change(instruction[1], [instruction[2], instruction[3]], '-')
        
    index += 1   
    if instruction[0] == 'JNE':
        value_1 = registers.to_int(instruction[2])
        value_2 = registers.to_int(instruction[3])
        # Jump.
        if value_1 != value_2:
            index = int(instruction[1])
        
    if index == len(instructions):
        next_instruction = ''
    else:
        next_instruction = instructions[index]
            
    #print(f'Next instruction: {next_instruction}', file = stderr)
    #print(f'a: {registers.a} ; b: {registers.b} ; c: {registers.c}; d: {registers.d}', file = stderr)
            
print(f'{registers.a} {registers.b} {registers.c} {registers.d}')
