def input_matrix(prompt):

    # 輸入矩陣並轉換為字典形式
    matrix_str = input(prompt)
    rows = matrix_str.split('|')
    matrix_dict = {}
    for i, row in enumerate(rows):
        matrix_dict[i] = [int(x) for x in row.split(',')]
    return matrix_dict

def matrix_multiply(U, V):
    
    # 計算矩陣乘法 U x V，結果以字典形式返回
    n = len(U)
    result = {i: [0] * n for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += U[i][k] * V[k][j]
    
    return result

def print_matrix(M):
    
    # 印出矩陣
    for i in range(len(M)):
        print(M[i])

# input
U = input_matrix("Enter matrix U: ")
V = input_matrix("Enter matrix V: ")

print("M = U x V")
M = matrix_multiply(U, V)
print_matrix(M)