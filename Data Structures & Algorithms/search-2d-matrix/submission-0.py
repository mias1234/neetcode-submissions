class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)

        # row = i / cols
        # col = i % cols


        left = 0; right = (cols * rows) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols; col = mid % cols
            print(f'(L,R) = ({left}:{right}), (Row,col) = ({row}:{col}), mid = {mid}, mid_el = {matrix[row][col]}')
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] == target:
                return True

        return False

