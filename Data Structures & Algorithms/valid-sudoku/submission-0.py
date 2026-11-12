class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}
        col_seen = {}

        for i, row in enumerate(board):
            row_seen = set()

            for j, n in enumerate(row):
                if n != ".":

                    # check for duplicates in row
                    if n in row_seen:
                        return False
                    else:
                        row_seen.add(n)

                    # check for duplicates in column
                    if j not in col_seen:
                        col_seen[j] = set()
                    else:
                        if n in col_seen[j]:
                            return False

                    col_seen[j].add(n)

                        
                
                    # check for duplicates in 3x3 sub-boxes
                    box = (j // 3, i // 3)
                    
                    if box not in boxes:
                        boxes[box] = set()
                    else:
                        if n in boxes[box]:
                            return False

                    boxes[box].add(n)
                    
                    
        
        return True