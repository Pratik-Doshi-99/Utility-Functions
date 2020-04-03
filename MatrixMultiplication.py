class MatrixMultiplication():
    
    def __init__(self):
        pass
    
    def get_element(self, col_index, m, row):
        s = 0
        for i, r in enumerate(m):
            s += r[col_index] * row[i]
        return s
    
    def multiply(self, m1, m2):
        #verify if the criteria is met
        if(len(m2)!=len(m1[0])):
            return 'INVALID MATRIX DIMENSIONS'
        l = len(m1[0])
        l2 = len(m2[0])
        for row in m1:
            if(len(row)!=l):
                return 'INVALID MATRIX DIMENSIONS'
        for row in m2:
            if(len(row)!=l2):
                return 'INVALID MATRIX DIMENSIONS'

        product = []
        for row in m1:
            temp_row = []
            for i in range(len(m2[0])):
                temp_row.append(get_element(i,m2,row))
            product.append(temp_row)
        return product
