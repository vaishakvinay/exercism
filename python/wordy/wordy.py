def answer(question):
    # 1. Must start with "What is"
    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    # 2. Remove fixed words and strip
    q = question[len("What is"):].strip()
    if q.endswith("?"):
        q = q[:-1].strip()

    if not q:
        raise ValueError("syntax error")  # Handles "What is?" and "What is ?"

    allowed_ops = {"plus", "minus", "multiplied", "divided"}
    tokens = q.split()

    # 3. Merge "multiplied by" and "divided by"
    merged = []
    i = 0
    while i < len(tokens):
        if tokens[i] in ("multiplied", "divided"):
            if i + 1 < len(tokens) and tokens[i + 1] == "by":
                merged.append(tokens[i] + " by")
                i += 2
                continue
            else:
                raise ValueError("syntax error")
        merged.append(tokens[i])
        i += 1
    tokens = merged

    # 4. Handle single token
    if len(tokens) == 1:
        if not tokens[0].lstrip("-").isdigit():
            raise ValueError("syntax error")
        return int(tokens[0])

    # 5. Validate tokens
    for t in tokens:
        if not (t.lstrip("-").isdigit() or t in allowed_ops or t in ("multiplied by", "divided by")):
            raise ValueError("unknown operation")

    # 6. Must alternate number / op / number
    if not tokens[0].lstrip("-").isdigit():
        raise ValueError("syntax error")  # Handles prefix notation

    expect_number = False
    for t in tokens[1:]:
        if expect_number:
            if not t.lstrip("-").isdigit():
                raise ValueError("syntax error")  # Missing number, consecutive ops
        else:
            if not (t in allowed_ops or t in ("multiplied by", "divided by")):
                raise ValueError("syntax error")  # Two numbers in a row
        expect_number = not expect_number

    if expect_number:
        raise ValueError("syntax error")  # Trailing operation

    # 7. Evaluate left-to-right
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = int(tokens[i + 1])
        if op == "plus":
            result += num
        elif op == "minus":
            result -= num
        elif op == "multiplied by":
            result *= num
        elif op == "divided by":
            if num == 0:
                raise ValueError("syntax error")
            result //= num
        i += 2

    return result








