class Matrix:

    def __init__(self, list1):
        self.list1 = list1

    def __str__(self):
        new_list1 = '\n'.join(map(str, self.list1))
        return new_list1

    def __add__(self, other):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.list1)):
            for k in range (len(other.list1)):
                matrix[i][k] = self.list1[i][k] +other.list1[i][k]
        return str('\n'.join([' '.join([str(k) for k in i]) for i in matrix]))

mat_1 = Matrix([[2, 3, 5], [2, 5, 2], [6, 1, 1]])
mat_2 = Matrix([[2, 3, 5], [2, 5, 2], [6, 1, 1]])

print(mat_1.__add__(mat_2))