class Matrix:
    def __init__(self, matrix_string):
        self.rows = []

        lines = matrix_string.split("\n")

        for line in lines:
            numbers = line.split()
            row = []

            for num in numbers:
                row.append(int(num))

            self.rows.append(row)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        col = []

        for row in self.rows:
            col.append(row[index - 1])

        return col
