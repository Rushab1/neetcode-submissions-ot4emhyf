class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        flip across horizonal center then take transpose 
        """

        def pprint(_matrix):
            for i in range(len(matrix)):
                print("\t".join([str(x) for x in matrix[i]]))
            print("")

        # pprint(matrix)

        # Flip: nxn: i j -> n-i-1, j
        n = len(matrix)
        for i in range(math.ceil(n / 2)):
            for j in range(n):
                matrix[i][j],  matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

        # transpose
        # pprint(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]

        # pprint(matrix)