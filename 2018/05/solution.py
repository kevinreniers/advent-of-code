import string


def is_opposite(first: str, second: str):
    if first.isupper() and second.islower() and first == second.upper():
        return True
    if first.islower() and second.isupper() and first == second.lower():
        return True
    return False


def is_unit(first: str, second: str):
    return first.upper() == second.upper()


def basic_react(polymer: str):
    while True:
        reaction = react(polymer)
        # print('Polymer={} Reaction={}'.format(len(polymer), len(reaction)))
        if reaction == polymer:
            return reaction
        polymer = reaction


def react(polymer: str):
    for char in string.ascii_lowercase:
        # print('Removing instances of', char + char.upper(), 'and', char.upper() + char)
        polymer = polymer.replace(char + char.upper(), '').replace(char.upper() + char, '')
    return polymer


def optimised_react(polymer: str):
    best_reaction = polymer
    for char in string.ascii_lowercase:
        reaction = polymer
        # print('Removing units', char, 'and', char.upper())
        reaction = reaction.replace(char, '').replace(char.upper(), '')
        reaction = basic_react(reaction)
        if len(best_reaction) > len(reaction):
            best_reaction = reaction
    return best_reaction


if __name__ == '__main__':
    with open(r'in.txt') as file:
        polymer = file.readline()

    print('Polymer Length (Part 1): ', len(basic_react(polymer)))
    print('Polymer Length (Part 2): ', len(optimised_react(polymer)))
