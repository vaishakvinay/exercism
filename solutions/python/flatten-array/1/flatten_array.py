def flatten(iterable):
    

    result = []

    for item in iterable:

        # If item is a list → flatten it recursively
        if isinstance(item, list):
            result.extend(flatten(item))

        # If item is None → ignore it
        elif item is None:
            continue

        # Otherwise → add to result
        else:
            result.append(item)

    return result