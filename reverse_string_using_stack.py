from stacks import Stack

def reverse_string(s: str) -> str:
    """
    Simple function to reverse a string using Stack.
    """
    stack = Stack()
    rev_s = ""

    # Push each character into stack
    for ch in s:
        stack.push(ch)

    # Pop from stack and append to string till stack is empty
    while not stack.is_empty():
        rev_s += stack.pop()

    return rev_s

if __name__ == "__main__":
    str_rev = reverse_string("We will conquer COVID-19")
    print(str_rev)

