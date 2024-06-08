def do_empty_transitions(current_state, transitions):
    for state in current_state:
        if state in transitions:
            if "vazio" in transitions[state]:
                current_state.extend(transitions[state]["vazio"])
    return current_state

symbols = input().split()
states = input().split()

transitions_count = int(input())
transitions = dict()
for i in range(transitions_count):
    transition = input().split()
    state = transition[0]
    symbol = transition[1]
    result = transition[2]

    if state not in transitions:
        transitions[state] = dict()

    if symbol not in transitions[state]:
        transitions[state][symbol] = []

    transitions[state][symbol].append(result)

initial_state = [input()]
final_states = input().split()
string_count = int(input())

for i in range(string_count):
    string = input()
    current_state = initial_state
    current_state = do_empty_transitions(current_state, transitions)
    for char in string:
        new_state = []
        for state in current_state:
            if state in transitions:
                if char in transitions[state]:
                    new_state.extend(transitions[state][char])
        current_state = new_state
        current_state = do_empty_transitions(current_state, transitions)
    accept = False
    for state in current_state:
        if state in final_states:
            accept = True
            break
    if accept:
        print("Aceita")
    else:
        print("Rejeita")
