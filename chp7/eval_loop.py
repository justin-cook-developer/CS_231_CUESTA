def eval_loop():
    msg = 'Enter a statement to evaluate or `done` to quit\n'
    toEval = input(msg)
    value = None

    while (toEval != 'done'):
        value = eval(toEval)
        print(value)
        toEval = input(msg)

    return value


print(eval_loop())
