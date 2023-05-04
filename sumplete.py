
class Sumplete:

    def __init__(self, matrix, rows_answers, cols_answers):
        self.matrix = matrix
        self.rows_answers = rows_answers
        self.cols_answers = cols_answers
        self.rows = [0 for _ in range(len(self.rows_answers))]
        self.cols = [0 for _ in range(len(self.cols_answers))]
        self.solved = False
        self.answer = [[False for _ in range(len(self.matrix))] for _ in range(len(self.matrix))]

    def solve(self):

        def dfs(r, c):
            if not (0 <= r < len(self.matrix) and 0 <= c < len(self.matrix[0])): return

            if self.solved:
                return

            val = self.matrix[r][c]
            
            if self.rows[r] + val <= self.rows_answers[r] and self.cols[c] + val <= self.cols_answers[c]:

                self.rows[r] += val
                self.cols[c] += val
                self.answer[r][c] = True

                if self.rows == self.rows_answers and self.cols == self.cols_answers:
                    self.solved = True
                    return

                if self.rows[r] == self.rows_answers[r]:
                    dfs(r+1, 0)
                else:
                    dfs(r,c+1)
                
                if not self.solved:
                    self.rows[r] -= val
                    self.cols[c] -= val
                    self.answer[r][c] = False

            dfs(r, c+1)
        dfs(0, 0)

                

                


            
