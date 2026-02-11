def is_paired(input_string):

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in input_string:

        
        if ch in "([{":
            stack.append(ch)

        
        elif ch in ")]}":

            if not stack:
                return False

            if stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0

