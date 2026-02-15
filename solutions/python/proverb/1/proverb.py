def proverb(*items, qualifier=None):

    if not items:
        return []

    lines = []

    for i in range(len(items) - 1):
        current = items[i]
        nex = items[i + 1]

        line = f"For want of a {current} the {nex} was lost."
        lines.append(line)

    # First item (after loop)
    first = items[0]

    if qualifier:
        first = f"{qualifier} {first}"

    lines.append(
        f"And all for the want of a {first}."
    )

    return lines
