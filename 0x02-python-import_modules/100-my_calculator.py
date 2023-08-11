#!/usr/bin/python3
def main():
    from sys import exit, argv
    import calculator_1
    
    # handling wrong number of arguments for the calculation
    element = len(argv)
    if not element == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # handling wrong operators
    operators = ["+", "-", "*", "/"]
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # handle calculation. Create a dict to handle the operator and operations
    a = int(argv[1])
    b = int(argv[3])
    operator_dic = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }
    operator = argv[2]
    if operator in operator_dic:
        result = operator_dic[operator]
        print("{} {} {} = {}".format(a, operator, b, result(a, b)))


if __name__ == "__main__":
    main()
