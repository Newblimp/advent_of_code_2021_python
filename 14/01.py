def polymerize(chain_str, rulebook):
    new_chain = ''
    for i in range(len(chain_str)-1):
        new_chain = new_chain + chain_str[i] + rulebook[chain_str[i:i+2]]
    new_chain = new_chain + chain_str[-1]
    return new_chain

def update_atom_freq(frq, frq_chains, rule_dict):
    for chain in frq_chains:
        if rule_dict[chain] not in frq:
            frq[rule_dict[chain]] = 0
        frq[rule_dict[chain]] += frq_chains[chain]
    return frq

def update_chain_freq(frq_chains, looping_rules):
    new_freq_chain = {}
    for chain in frq_chains:
        if looping_rules[chain][0] not in new_freq_chain:
            new_freq_chain[looping_rules[chain][0]] = 0
        if looping_rules[chain][1] not in new_freq_chain:
            new_freq_chain[looping_rules[chain][1]] = 0
        new_freq_chain[looping_rules[chain][0]] += frq_chains[chain]
        new_freq_chain[looping_rules[chain][1]] += frq_chains[chain]
    return new_freq_chain

def get_freq(chain_str):
    counter = {}
    for c in chain_str:
        if c not in counter.keys():
            counter[c] = 0
        counter[c] += 1
    return counter

def get_freq_chains(chain_str):
    counter = {}
    for i in range(len(chain_str)-1):
        if chain_str[i:i+2] not in counter.keys():
            counter[chain_str[i:i+2]] = 0
        counter[chain_str[i:i+2]] += 1
    return counter


def most_min_least_common(diction):
    most = 0
    least = diction['B']
    for item in diction:
        if diction[item] > most:
            most = diction[item]
        if diction[item] < least:
            least = diction[item]
    return most - least

def rule_translator(rules_dict):
    loops = {}
    for str in rules_dict:
        loops[str] = [str[0] + rules_dict[str], rules_dict[str] + str[1]]
    return loops

with open("14/input.txt","r") as file:
    start_chain = file.readline().strip()
    rules_str = file.readlines()
    rules_str.pop(0)

rules = {}
for line in rules_str:
    rules[line[:2]] = line[6]

loop_rules = rule_translator(rules)

freq = get_freq(start_chain)
freq_chains = get_freq_chains(start_chain)
# print(freq_chains)
# print(freq)

for i in range(40):
    freq = update_atom_freq(freq, freq_chains, rules)
    freq_chains = update_chain_freq(freq_chains, loop_rules)

print(freq)
# for i in range(10):
#     next_chain = polymerize(start_chain, rules)
#     start_chain = next_chain
result = most_min_least_common(freq)
print(result)