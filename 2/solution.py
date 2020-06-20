import csv


# Phase 1
# -------------------------------------

def phase_1(filename):
    nums = []
    with open(filename) as fin:
        for line in fin:
            nums.append(int(line))

    answer = sum(nums)
    print(f'Sum is: {answer}')  # f-strings are sometimes easier than concatenation


# Phase 2
# -------------------------------------

def phase_2(filename):
    profit = 0
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            revenue = int(row['revenue'])
            cost = int(row['cost'])

            profit += revenue - cost

    print(f'Net profit: {profit}')


# Run all solutions
# -------------------------------------

print('Phase 1...')
phase_1('data/phase_1.txt')
print()

print('Phase 2...')
phase_2('data/phase_2.csv')
print()
