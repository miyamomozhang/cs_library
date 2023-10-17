""" 73. 矩阵置零
https://leetcode.cn/problems/set-matrix-zeroes/

给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。 """

from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = [0] * m
        columns = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    columns[j] = 1
        for i, row in enumerate(rows):
            if row == 1:
                matrix[i] = [0] * n
        for j, column in enumerate(columns):
            if column == 1:
                matrix[:][j] = [0] * m
