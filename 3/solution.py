y = input('> ')


def derive(term):
    try:
        x_idx = term.index('x')
    except ValueError:
        return None

    try:
        exp_idx = term.index('^')
        exp = int(term[exp_idx+1])
    except ValueError:
        exp = 1

    const = int(term[:x_idx])

    if exp-1 == 0:
        ending = ''
    elif exp-1 == 1:
        ending = 'x'
    else:
        ending = f'x^{exp-1}'

    new_term = f'{const * exp}{ending}'

    return new_term


terms = y.replace(' ', '').split('+')

der_terms = []
for t in terms:
    dt = derive(t)
    if dt is not None:
        der_terms.append(dt)

if len(der_terms) == 0:
    print('0')
else:
    print(' + '.join(der_terms))

