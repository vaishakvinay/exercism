def tick(matrix):
    

    result=[]
    
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        new_row = []

        for col in range(cols):
            live_neighbors = 0

            for r in [-1, 0, 1]:
                for c in [-1, 0, 1]:

                    if r == 0 and c == 0:
                        continue

                    new_r = row + r
                    new_c = col + c

                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if matrix[new_r][new_c] == 1:
                            live_neighbors += 1
                            
            current = matrix[row][col]

            if current == 1 and (live_neighbors == 2 or live_neighbors == 3):
                new_row.append(1)
            elif current == 0 and live_neighbors == 3:
                new_row.append(1)
            else:
                new_row.append(0)

        result.append(new_row)

    return result