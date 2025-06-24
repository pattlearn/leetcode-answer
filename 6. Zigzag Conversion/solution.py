class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        curr_row = 0
        incrment = True        
        row_dict = {}
        
        for row in range(numRows):
            row_dict[row] = []
        
        for i in s:
            row_dict[curr_row].append(i)
            
            if curr_row == 0:
                increment = True
            elif curr_row ==  numRows - 1:
                increment = False
                
            if increment:
                curr_row += 1
            else:
                curr_row -= 1
        
        list_prod = []
        for row in row_dict:
            list_prod += row_dict[row]
        out_str = "".join(list_prod)
        
        return out_str