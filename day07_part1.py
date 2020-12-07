
# fname = 'inputs/day07.test.txt'
fname = 'inputs/day07.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]


def bag_info(str):
    number, *color, _ = str.split(' ')
    return(' '.join(color), int(number))

bags_rules = {}
for rule in lines:
    bag_color, bag_contents = rule.split(' bags contain ')
    if not bag_contents.startswith('no other bag'):
        bags_rules[bag_color] = dict(bag_info(content) for content in bag_contents.split(', '))


valid_colors = set()
new_valid = {bag for bag,contents in bags_rules.items() if 'shiny gold' in contents}
while new_valid:
    valid_colors |= new_valid
    new_valid = {bag for bag,contents in bags_rules.items() if any(newbag in contents for newbag in new_valid)}

print(len(valid_colors))
