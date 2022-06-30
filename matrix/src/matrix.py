class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        row_list = []
        for character in self.matrix_string:
            if character.isdigit():
                row_list.append(int(character))
        return row_list[:index]

    def column(self, index):
        pass
