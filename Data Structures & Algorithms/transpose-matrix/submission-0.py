class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M = len(matrix)
        N = len(matrix[0])
        
        new_matrix = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(M):
            for j in range(N):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix