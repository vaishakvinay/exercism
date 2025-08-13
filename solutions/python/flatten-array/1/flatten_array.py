def flatten(iterable):
    flat = []
    for item in iterable:
        if item is None:
            # Skip null values
            continue
        # Check if item is iterable but NOT a string (strings should be treated as elements)
        if isinstance(item, (list, tuple)):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat