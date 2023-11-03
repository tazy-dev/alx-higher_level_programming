#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    func = {"+": add, "-": sub, "*": mul, "/": div}
    op1, op, op2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if op in list(func.keys()):
        print("{} {} {} = {}".format(op1, op, op2, func[op](op1, op2)))
    else:
        print("Unknown operator.  Available operators: +, -, *, and /")
        sys.exit(1)
