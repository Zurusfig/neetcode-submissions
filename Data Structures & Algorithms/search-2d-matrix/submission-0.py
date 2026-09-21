class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l,r = 0, len(matrix) - 1
        while l <= r:
            m = l + ((r-l) // 2)
            mr = matrix[m]
            if mr[-1] < target:
                l = m + 1
            elif mr[0] > target:
                r = m -1
            else:
                cl, cr = 0, len(mr) - 1
                while cl <= cr:
                    cm = cl + ((cr-cl) // 2)
                    if mr[cm] > target:
                        cr = cm -1
                    elif mr[cm] < target:
                        cl = cm + 1
                    else:
                        return True
                return False
        return False


            
            
        