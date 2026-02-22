"""Flower Field annotation."""

def annotate(garden):
    """Return the garden with flower counts annotated."""


    if not garden:
        return []

    row_length = len(garden[0])

    for row in garden:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")

        for cell in row:
            if cell not in ("*", " "):
                raise ValueError("The board is invalid with current input.")

    rows = len(garden)
    cols = row_length
    result = []

    for row_index in range(rows):
        new_row = []

        for col_index in range(cols):
            flower_count = 0

            for row_offset in (-1, 0, 1):
                for col_offset in (-1, 0, 1):

                    if row_offset == 0 and col_offset == 0:
                        continue

                    neighbor_row = row_index + row_offset
                    neighbor_col = col_index + col_offset

                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        if garden[neighbor_row][neighbor_col] == "*":
                            flower_count += 1

            current_cell = garden[row_index][col_index]

            if current_cell == "*":
                new_row.append("*")
            else:
                if flower_count == 0:
                    new_row.append(" ")
                else:
                    new_row.append(str(flower_count))

        result.append("".join(new_row))

    return result