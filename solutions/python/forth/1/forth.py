class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def evaluate(input_data):

    stack = []
    definitions = {}

    def execute(token):
       
        if token in definitions:
            for sub in definitions[token]:
                execute(sub)
            return

        
        if token in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                raise StackUnderflowError(
                    "Insufficient number of items in stack"
                )

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(a // b)
            return

       
        if token == "dup":
            if len(stack) < 1:
                raise StackUnderflowError(
                    "Insufficient number of items in stack"
                )
            stack.append(stack[-1])
            return

        if token == "drop":
            if len(stack) < 1:
                raise StackUnderflowError(
                    "Insufficient number of items in stack"
                )
            stack.pop()
            return

        if token == "swap":
            if len(stack) < 2:
                raise StackUnderflowError(
                    "Insufficient number of items in stack"
                )
            stack[-1], stack[-2] = stack[-2], stack[-1]
            return

        if token == "over":
            if len(stack) < 2:
                raise StackUnderflowError(
                    "Insufficient number of items in stack"
                )
            stack.append(stack[-2])
            return

        
        if token.lstrip("-").isdigit():
            stack.append(int(token))
            return

        # Undefined word
        raise ValueError("undefined operation")

    for line in input_data:
        tokens = line.lower().split()
        i = 0

        while i < len(tokens):
            token = tokens[i]

         
            if token == ":":
                i += 1
                if i >= len(tokens):
                    raise ValueError("illegal operation")

                word_name = tokens[i]

               
                if word_name.lstrip("-").isdigit():
                    raise ValueError("illegal operation")

                definition = []
                i += 1

                while i < len(tokens) and tokens[i] != ";":
                    word = tokens[i]


                    if word in definitions:
                        definition.extend(definitions[word])
                    else:
                        definition.append(word)

                    i += 1

                if i >= len(tokens) or tokens[i] != ";":
                    raise ValueError("illegal operation")

                definitions[word_name] = definition

            else:
                execute(token)

            i += 1

    return stack