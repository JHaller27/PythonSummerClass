# Phase 1
# -------------------------------------

def phase_1(filename):
    nums = []
    with open(filename) as fin:
        for line in fin:
            nums.append(int(line))

    answer = sum(nums)
    print(f'Sum is: {answer}')  # f-strings are sometimes easier than concatenation


# Run all solutions
# -------------------------------------

phase_1('data/phase_1.txt')
