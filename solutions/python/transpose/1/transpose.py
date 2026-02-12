def transpose(text):
    
    rows = text.split("\n")

    if not rows:
        return ""

    max_len = max(len(row) for row in rows)

    result = []

    for col in range(max_len):
        new_row = ""

        for r in range(len(rows)):
            if col < len(rows[r]):
                new_row += rows[r][col]
            else:
                # Add space only if later rows have characters
                for later in rows[r:]:
                    if col < len(later):
                        new_row += " "
                        break

        result.append(new_row)

    return "\n".join(result)