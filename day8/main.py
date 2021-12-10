lines = [line.split(' | ') for line in open("day8/input").read().strip().split("\n")]
parsed = [(line[0].split(' '), line[1].split(' ')) for line in lines]

def count_unique_outputs(outputs):
    return sum([1 for output in outputs if len(output) in [2,3,4,7]])

def a_contains_b(a, b):
    return len([c for c in b if c in a]) == len(b)

def a_without_b(a, b):
    return "".join([c for c in a if c not in b])

def deduce_numbers(signals):
    digit_map = {}
    known_map = {}

    # Parse knowns
    for signal in ["".join(sorted(s)) for s in signals if len(s) not in [5,6]]:
        if len(signal) == 2:
            digit_map[signal] = '1'
            known_map["1"] = signal
        elif len(signal) == 4:
            digit_map[signal] = '4'
            known_map["4"] = signal
        elif len(signal) == 3:
            digit_map[signal] = '7'
            known_map["7"] = signal
        elif len(signal) == 7:
            digit_map[signal] = '8'
            known_map["8"] = signal
    
    # deduce unknowns
    for signal in ["".join(sorted(s)) for s in signals if len(s) in [5,6]]:
        if len(signal) == 5:
            if a_contains_b(signal, known_map["1"]):
                digit_map[signal] = '3'
            elif a_contains_b(signal, a_without_b(known_map["4"], known_map["1"])):
                digit_map[signal] = '5'
            else:
                digit_map[signal] = '2'
        elif len(signal) == 6:
            if not a_contains_b(signal, known_map["1"]):
                digit_map[signal] = '6'
            elif a_contains_b(signal, known_map["4"]):
                digit_map[signal] = '9'
            else:
                digit_map[signal] = '0'
    
    return digit_map

def decode_output(signals, output):
    digit_map = deduce_numbers(signals)
    return int("".join([digit_map["".join(sorted(o))] for o in output]))

print(sum([count_unique_outputs(line[1]) for line in parsed]))
print(sum([decode_output(line[0], line[1]) for line in parsed]))