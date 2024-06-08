symbols = input().split()

states = input().split()
state_transitions = dict()

num_transitions = int(input())
for i in range(num_transitions):
    transition = input().split()
    state = transition[0]
    symbol = transition[1]
    result = transition[2]
    if state not in state_transitions:
        state_transitions[state] = dict()
    state_transitions[state][symbol] = result

initial_state = input()
final_states = input().split()
string_tests = int(input())

for i in range(string_tests):
    current_state = initial_state
    string = input()
    for char in string:
        current_state = state_transitions[current_state][char]
    if current_state in final_states:
        print("Aceita")
    else:
        print("Rejeita")
