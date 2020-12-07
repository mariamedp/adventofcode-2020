
# fname = 'inputs/day07.test.txt'
# fname = 'inputs/day07.test2.txt'
fname = 'inputs/day07.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]


def bag_info(str):
    number, *color, _ = str.split(' ')
    return(' '.join(color), int(number))

bags_rules = {}
for rule in lines:
    bag_color, bag_contents = rule.split(' bags contain ')
    bags_rules[bag_color] = None if bag_contents.startswith('no other bag') else dict(bag_info(content) for content in bag_contents.split(', '))


def count_bags_inside(bag_color):
    contents = bags_rules[bag_color]
    if contents is None:
        return 0
    else:
        return sum(n * (1 + count_bags_inside(b)) for b,n in contents.items())
    
total_bags = count_bags_inside('shiny gold')
print(total_bags)
