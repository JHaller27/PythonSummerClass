def run_once() -> bool:
    o1 = input('#1> ')

    if o1 == 'exit':
        return False

    o2 = input('#2> ')
    op = input('op> ')

    o1 = int(o1)
    o2 = int(o2)

    if op == '+':
        print(o1 + o2)
    elif op == '-':
        print(o1 - o2)
    elif op == '*':
        print(o1 * o2)
    elif op == '/':
        print(o1 / o2)

    return True

def main():
    lcv = run_once()
    while lcv:
        lcv = run_once()

main()

