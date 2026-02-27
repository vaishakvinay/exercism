def saddle_points(matrix):
    result = []

    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Check for irregular matrix
    for row in matrix:
        if len(row) != cols:
            raise ValueError("irregular matrix")

    for r in range(rows):
        for c in range(cols):
            value = matrix[r][c]

            row_max = max(matrix[r])
            col_min = min(matrix[i][c] for i in range(rows))

            if value == row_max and value == col_min:
                result.append({"row": r + 1, "column": c + 1})

    return result