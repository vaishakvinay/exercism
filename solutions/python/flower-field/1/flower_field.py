def annotate(garden):
    if not garden:
        return []

    rows = len(garden)
    cols = len(garden[0])

    # Validate input board shape and characters
    for row in garden:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")
        if any(ch not in ('*', ' ') for ch in row):
            raise ValueError("The board is invalid with current input.")

    def count_flowers(r, c):
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if (dr != 0 or dc != 0) and 0 <= nr < rows and 0 <= nc < cols:
                    if garden[nr][nc] == '*':
                        count += 1
        return count

    result = []
    for r in range(rows):
        new_row = ''
        for c in range(cols):
            if garden[r][c] == '*':
                new_row += '*'
            else:
                flowers = count_flowers(r, c)
                new_row += str(flowers) if flowers > 0 else ' '
        result.append(new_row)

    return result
