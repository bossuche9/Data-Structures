"""
Week 4 Code:
    - Infix-Prefix conversion
    - A better queue

"""
import operator
from typing import Any
from pythonds3.basic import Stack

PREC = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}


OPER = {'^': operator.pow,
        '*': operator.mul,
        '/': operator.ifloordiv,
        '+': operator.add,
        '-': operator.sub}

def infix_to_postfix(infix_expr):
    """Returns the postfix string

    >>> infix_to_postfix('A * B + C * D')
    'A B * C D * +'

    """
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split() # .split puts words of a string into  seperate elements of a list
    previous_token =None

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":   # if we find a ( push it into the stack
            op_stack.push(token)
        elif token == ")":
            if  not op_stack.is_empty() and top_token != "(":
                return False
                
            top_token = op_stack.pop()
            while top_token != "(":  # if we find ) and the top of the stack is not (
                postfix_list.append(top_token)  # add them number of letter to the post fix expression
                top_token = op_stack.pop() 
        else:
            while (not op_stack.is_empty()) and \
                (PREC[op_stack.peek()] >= PREC[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


def postfix_eval(postfix_expr, environment):
    """Returns the integer value of the postfix expression

    Letter tokens are assumed to be uppercase letters.
    Numeric tokens are assumed to be single digit integers

    Args:
        postfix_expr (str): expression to be evaluated
        environment (dict[str, int]): evaluation environment for letter tokens

    >>> sym_table = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
    >>> postfix_eval('A B * C D * +', sym_table)
    1400
    """
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":    # if it is an operand
            operand_stack.push(int(token))  # push it to the top of the stack
        elif token in OPER:
            if OPER == '/' and operand2 == "0":  
                print("You cannot divide by 0")
                return False
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = OPER[token](operand1, operand2)
            operand_stack.push(result)
        else:
            operand_stack.push(environment[token])
    return operand_stack.pop()

class Queue:
    """A more efficient queue (on average)
    """
    def __init__(self) -> None:
        """Create new queue"""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Check if the queue is empty"""
        return NotImplemented

    def enqueue(self, item: Any) -> None:
        """Add an item to the queue"""
        raise NotImplementedError

    def dequeue(self) -> Any:
        """Remove an item from the queue"""
        return NotImplemented

    def size(self) -> int:
        """Get the number of items in the queue"""
        return NotImplemented


if __name__ == "__main__":
    import doctest
    doctest.testmod()
