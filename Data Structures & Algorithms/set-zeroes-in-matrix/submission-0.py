class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Eadge cases when I recive only one row
        # [[1,0,3]]
        if len(matrix) == 1:
            # We only have one row
            for col in range(len(matrix[0])):
                if matrix[0][col] == 0:
                    for i in range(len(matrix[0])):
                        matrix[0][i] = 0
                    return
            return
        # Edge case wher I recive only one col
        # [[1], 
        #  [0], 
        #  [3]]
        if len(matrix[0]) == 1:
            # We only have one col
            for row in range(len(matrix)):
                if matrix[row][0] == 0:
                    for i in range(len(matrix)):
                        matrix[i][0] = 0
                    return
            return
        # matrix =
        # [[1,1,1],
        #  [1,0,1],
        #  [1,1,1]]

        # Failed case:
        # Input: 
        # [[   -4     ,-2147483648, 6,-7, 0],
        #  [   -8     ,     6     ,-8,-6, 0],
        #  [2147483647,     2     ,-9,-6,-10]]
        
        # Output:
        # [[    0     ,     0     , 0, 0, 0],
        #  [    0     ,     0     , 0, 0, 0],
        #  [2147483647,     2     ,-9,-6, 0]]

        # My output:
        # [[    0     ,-2147483648, 6,-7,0],
        #  [    0     ,     0     , 0, 0,0],
        #  [2147483647,     2     ,-9,-6,0]]

        # New failed case:
        # [[1 ,2 ,3 ,4 ],
        #  [5 ,0 ,7 ,8 ],
        #  [0 ,10,11,12],
        #  [13,14,15,0 ]]

        # Output
        # [[0,0,3,0],
        #  [0,0,0,0],
        #  [0,0,0,0],
        #  [0,0,0,0]]

        # My output:
        # [[0,0,0,0],
        #  [0,0,0,0],
        #  [0,0,0,0],
        #  [0,0,0,0]]

        zero_in_row_one = False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                zero_in_row_one = True
                break
        zero_in_col_one = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zero_in_col_one = True
                break

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        # Once all zeros have been marked
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[row])):
                    matrix[row][col] = 0
        print('Flags in first and second row marked', matrix)
        # Check if i need to replace the first col and row
        if zero_in_row_one:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if zero_in_col_one:
            for i in range(len(matrix)):
                matrix[i][0] = 0   
        

        