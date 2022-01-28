from stacks import Stack

def is_balanced(s: str) -> bool:
    """
    Function to check is parenthesis are balanced using Stack/dequeue
    """
    open_parenthesis = "({["
    closing_parenthesis = ")}]"
    parenthesis_dict = {"(":")", "{":"}", "[":"]"}
    stack = Stack()

    for ch in s:
        if ch in open_parenthesis:
            stack.push(parenthesis_dict[ch])
        elif ch in closing_parenthesis:
            if stack.pop() == ch:
                continue
            else:
                return False
        else:
            continue
    
    if stack.is_empty():
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


