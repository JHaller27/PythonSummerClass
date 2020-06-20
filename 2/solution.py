import csv
import os


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


# Phase 3
# -------------------------------------

def list_files(directory_name):
    '''
    Generator function that returns the names of all files in a directory
    '''
    for f in os.listdir(directory_name):
        full_path = os.path.join(directory_name, f)
        if os.path.isfile(full_path):
            yield full_path


def get_client_sums(csv_reader, min_year, max_year):
    sums = {}

    for row in csv_reader:
        year = int(row['year'])

        if min_year <= year <= max_year:
            amt = float(row['amount'])

            if year in sums:
                sums[year] += amt
            else:
                sums[year] = amt

    return sums


def phase_3(dir_name):
    year_sums = []

    print('Progress: ', end='')
    for path in list_files(dir_name):
        with open(path) as fin:
            # Print a dot for each opened file (so that we know the program is progressing)
            print('.', end='')

            reader = csv.DictReader(fin)
            client_sums = get_client_sums(reader, 2014, 2019)

        # Add each year-sum to the list of sums for all clients
        for year in client_sums:
            year_sums.append(client_sums[year])
    print()

    avg_per_year = sum(year_sums) / len(year_sums)

    # The weird stuff after the : in the brackets
    #  will format a float to have 2 digits after the decimal
    print(f'Average per year: {avg_per_year:.2f}')


# Run all solutions
# -------------------------------------

print('Phase 1...')
phase_1('data/phase_1.txt')
print()

print('Phase 2...')
phase_2('data/phase_2.csv')
print()

print('Phase 3...')
phase_3('data/reports')
print()
