'''Given an m x n grid of characters board and a string word, return true if word exists in
the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent
cells are horizontally or vertically neighboring. The same letter cell may not be used
more than once'''

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        # If all characters are matched
        if i == len(word):
            return True
        
        # Boundary + mismatch check
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
        
        # Mark as visited
        temp = board[r][c]
        board[r][c] = "#"
        
        # Explore all 4 directions
        found = (dfs(r+1, c, i+1) or
                 dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or
                 dfs(r, c-1, i+1))
        
        # Restore original value (backtrack)
        board[r][c] = temp
        
        return found

    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    
    return False


# Example
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "ABCCED"

print(exist(board, word))  # Output: True