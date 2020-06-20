import random


def gen_transaction_count():
    return (random.randint(1,20) + random.randint(1,20)) * 1000 + random.randint(0, 999)

# Wealth score vs cost per transaction
WEALTH = [ 2, 5, 10, 15, 20, 50, 100 ]

def gen_wealth_score():
    return sum([random.randint(0, 1) for _ in range(len(WEALTH) - 1)])

def gen_transaction(wealth_score):
    avg_transaction = WEALTH[wealth_score]
    roll = random.randint(1,200)

    # Large income
    if roll == 1:
        avg_large_income = avg_transaction * 230
        return random.gauss(avg_large_income, avg_large_income * 0.1)

    # Small income
    if roll == 2:
        return random.gauss(avg_transaction, avg_transaction * 0.1)

    # Charge
    return -1 * random.gauss(avg_transaction, avg_transaction * 0.1)

def gen_client_ids(count):
    dig_per_id = 16
    used_ids = set()
    while len(used_ids) < count:
        next_id = random.randint(10**(dig_per_id-1), 10**(dig_per_id)-1)
        if next_id not in used_ids:
            used_ids.add(next_id)
            yield next_id

def random_date(start_year):
    year = random.randint(start_year, 2019)
    month = random.randint(1, 12)

    if month == 2:
        if year % 4 == 0:
            days = 29
        else:
            days = 28
    elif month in [1,3,5,7,8,10,12]:
        days = 31
    else:
        days = 30

    day = random.randint(1, days)

    return year, month, day


for cid in gen_client_ids(100):
    wealth_score = 3
    client_since = random.randint(2008, 2018)

    fname = f'report-{client_since}-{cid}'
    path = f'data/reports/{fname}.csv'
    with open(path, 'w+') as fout:
        print(f'Writing to {path}...')

        fout.write('year,month,day,amount\n')

        for _ in range(gen_transaction_count()):
            y, m, d = random_date(client_since)
            amt = gen_transaction(wealth_score)

            fout.write(f'{y},{m},{d},{amt:.2f}\n')
