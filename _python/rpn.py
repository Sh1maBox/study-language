from typing import List
from operator import add, sub, mul, truediv

operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def evaluate_formula(formula: str) -> int:
    """rpn式を評価する関数

    Args:
        formula: rpn数式
    Return:
        result: 評価後の式
    """
    formula_list: List[str] = formula.split(" ")
    stack = []
    for c in formula_list:
        if c in operators:
            x, y = stack.pop(), stack.pop()
            stack.append(operators[c](y, x))
        else:
            stack.append(int(c))

    return stack[0]


if __name__ == "__main__":
    print(evaluate_formula("10 5 + 15 3 / *"))
