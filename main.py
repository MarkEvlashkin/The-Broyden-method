from math import sqrt
import sys
a = float(input("Введите a: "))
b = float(input("Введите b: "))
M = float(input("Введите M: "))
e = float(input("Введите e: "))
x0 = float(input("Введите начальное значение для x: "))
y0 = float(input("Введите начальное значение для y: "))
chek_broyden = 1
k = 0
n = 0
J = [
        [2*x0,  2*y0],
        [a, b]
    ]
F = [
        pow(x0,2)+ pow(y0,2) - M, 
        a*x0 + b*y0 - 1
    ]
X = [x0,y0]

def transpose_matrix(matrix):
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

def inv_matrix(matrix):
    i, j = 0, 0
    determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    if determinant == 0 or determinant == -0.0:
        print("Внимание! Вы ввели некорректные значения. Детерминант матрицы равен 0")
        chek_broyden = 0
        sys.exit()
        return chek_broyden
    determinant = 1/determinant
    inverse_matrix = transpose_matrix(matrix)
    copy_matrix = inverse_matrix
    inverse_matrix=[
            [copy_matrix [1][1], copy_matrix [1][0]],
            [copy_matrix [0][1], copy_matrix [0][0]]
            ]
    
    inverse_matrix=[
            [inverse_matrix [0][0]*pow(-1,2), inverse_matrix [0][1]*pow(-1,3)],
            [inverse_matrix [1][0]*pow(-1,3), inverse_matrix [1][1]*pow(-1,4)]
            ]

    for i in range(len(inverse_matrix)):
        for j in range(len(inverse_matrix)):
            
            inverse_matrix[i][j] = determinant * inverse_matrix[i][j]

    return inverse_matrix

def multiplay_matrix(matrix_1,matrix_2):
    multiplay_matrix = [matrix_1[0][0]*matrix_2[0]+matrix_1[0][1]*matrix_2[1],matrix_1[1][0]*matrix_2[0]+matrix_1[1][1]*matrix_2[1]]
    return multiplay_matrix
    
while chek_broyden == 1:
    #Находим обратную матрицу Якоби
  
    J_mult = [[J[0][0]*-1,J[0][1]*-1],[J[1][0]*-1,J[1][1]*-1]]
    
    J_inv = inv_matrix(J_mult)
    s = multiplay_matrix(J_inv,F)
  
    new_X = [X[0]+s[0],X[1]+s[1]]
    
    n = n + 1
    
    if sqrt(pow(s[0],2)+pow(s[1],2)) < e: 
        print("Значения X:",new_X)
        print("Количество итераций: ",n)
        chek_broyden = 0

    new_F = [
        pow(new_X[0],2)+ pow(new_X[1],2) - M, 
        a*new_X[0] + b*new_X[1] - 1
    ]

    def_F = [new_F[0]-F[0],new_F[1]-F[1]]
    mulyiplai_s = pow(s[0],2) + pow(s[1],2)
    if mulyiplai_s == 0 or mulyiplai_s == -0.0:
        print("Внимание! Вы ввели некорректные значения")
        chek_broyden = 0
        sys.exit()
    mulyiplai_J_s = multiplay_matrix(J,s)
    def_F_J_s = [def_F[0]-mulyiplai_J_s[0],def_F[1]-mulyiplai_J_s[1]]
    var = [[def_F_J_s[0]*s[0],def_F_J_s[0]*s[1]],[def_F_J_s[1]*s[0],def_F_J_s[1]*s[1]]]


    
    var = [[var[0][0]/mulyiplai_s,var[0][1]/mulyiplai_s],[var[1][0]/mulyiplai_s,var[1][1]/mulyiplai_s]]
    new_J = [[J[0][0]+var[0][0],J[0][1]+var[0][1]],[J[1][0]+var[1][0],J[1][1]+var[1][1]]]
   
    k = k + 1
    X = new_X
    F = new_F
    J = new_J

    if k == 100:
        print("Внимание! Количество итераций превышено")
        chek_broyden = 0
 

