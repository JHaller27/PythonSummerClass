def run_once():
    '''
    Get input from the user and perform math.
    Returns True if the program should end. Otherwise, returns False.
    '''

    # Get the first number, which may be "exit"
    o1 = input('#1> ')

    # If the user entered "exit", return True, meaning stop
    if o1 == 'exit':
        return True

    # If we're still here, that means the first number isn't "exit"

    # Get the second number and the operation
    o2 = input('#2> ')
    op = input('op> ')

    # Convert the operands to integers
    o1 = int(o1)
    o2 = int(o2)

    # Decide which operation to perform and print the result
    if op == '+':
        print(o1 + o2)
    elif op == '-':
        print(o1 - o2)
    elif op == '*':
        print(o1 * o2)
    elif op == '/':
        print(o1 / o2)

    return False


done = run_once()
while not done:
    done = run_once()
