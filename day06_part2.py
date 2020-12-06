
# fname = 'inputs/day06.test.txt'
fname = 'inputs/day06.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

nyes = []
group_questions = None
for person_questions in lines + ['']:
    if person_questions:
        if group_questions is None:
            group_questions = set(person_questions)
        else:
            group_questions &= set(person_questions)
    else:
        nyes.append(len(group_questions))
        group_questions = None

print(sum(nyes))
