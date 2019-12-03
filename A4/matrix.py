#--------------------------
# Nicolas Ross 151703880
# CP460 (Fall 2019)
# Assignment 4
#--------------------------

import math
import string
import mod

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid vector
#               A valid vector is a list in which all elements are integers
#               An empty list is a valid vector
# Errors:       None
#-----------------------------------------------------------
def is_vector(A):
    if type(A) is list:
        for i in range(len(A)):
            if type(A[i]) is not int:
                return False
        
        return True
    return False
#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid matrix
#               A matrix is a list in which all elements are valid vectors of equal size
#               Any valid vector is also a valid matrix
# Errors:       None
#-----------------------------------------------------------
def is_matrix(A):
    if is_vector(A):
        return True
    
    if type(A) is list:
        for a in A:
            if not is_vector(a):
                return False
            
            if is_vector(a) and len(a) != len(A[0]):
                return False

        return True

    return False

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       None
# Description:  Prints a given matrix, each row on a separate line
# Errors:       If A not a matrix --> print 'Error (print_matrix): Invalid input'
#-----------------------------------------------------------
def print_matrix(A):
    # your code here
    if is_matrix(A):
        for x in A:
            print(x)
    else:
        return 'Error (print_matrix): Invalid input'
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of rows (int)
# Description:  Returns number of rows in a given matrix
# Examples:     [5,3,2] --> 1
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 3
# Errors:       If A not a matrix -->
#                   return 'Error (get_rowCount): invalid input'
#-----------------------------------------------------------
def get_rowCount(A):
    if is_matrix(A):
        if len(A) == 0:
            return 0
            
        if is_vector(A):
            return 1

        return len(A)

    return 'Error (get_rowCount): invalid input'

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of columns (int)
# Description:  Returns number of columns in a given matrix
# Examples:     [5,3,2] --> 3
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 2
# Errors:       If A not a matrix -->
#                   return 'Error (get_columnCount): invalid input'
#-----------------------------------------------------------
def get_columnCount(A):
    if is_matrix(A):
        if len(A) == 0:
            return 0
        
        if is_vector(A):
            return len(A)

        return len(A[0])

    return 'Error (get_columnCount): invalid input'

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       [number of rows (int), number of columns(int)]
# Description:  Returns number size of matrix [rxc]
# Examples:     [5,3,2] --> [1,3]
#               [] --> [0,0]
#               [[1,2],[3,4],[5,6]] --> [3,2]
# Errors:       If A not a matrix -->
#                   return 'Error (get_size): invalid input'
#-----------------------------------------------------------
def get_size(A):
    if is_matrix(A):
        return [get_rowCount(A), get_columnCount(A)]

    return 'Error (get_size): invalid input'

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid square matrix
# Examples:     [] --> True
#               [10] --> True
#               [[1,2],[3,4]] --> True
#               [[1,2],[3,4],[5,6]] --> False
# Errors:       None
#-----------------------------------------------------------
def is_square(A):
    size = get_size(A)

    return size[0] == size[1]

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
# Return:       row (list)
# Description:  Returns the ith row of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1,2],[3,4]],0) --> [1,2]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_row): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error (get_row): invalid row number'
#-----------------------------------------------------------
def get_row(A,i):
    rows = get_rowCount(A)
    
    if type(rows) == int:
        if rows == 0:
            return 'Error (get_row): invalid input matrix'

        if rows <= i:
            return 'Error (get_row): invalid row number'

        return A[i]
    
    return 'Error (get_row): invalid input matrix'

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               j (column number)
# Return:       column (list)
# Description:  Returns the jth column of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1], [2]],0) --> [[1], [2]]
#               ([[1,2],[3,4]],1) --> [2,4]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_column): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error (get_column): invalid column number'
#-----------------------------------------------------------
def get_column(A,j):
    cols = get_columnCount(A)

    if type(cols) == int:
        if cols == 0:
            return 'Error (get_column): invalid input matrix'

        if cols <= j:
            return 'Error (get_column): invalid column number'

        col = []
        for i in range(len(A)):
            col.append([A[i][j]])

        return col
    
    return 'Error (get_column): invalid input matrix' 

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
#               j (column number)
# Return:       element
# Description:  Returns element (i,j) of the given matrix
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_element): invalid input matrix'
#               If i or j is outside matrix range -->
#                   return 'Error (get_element): invalid element position'
#-----------------------------------------------------------
def get_element(A,i,j):
    rows = get_rowCount(A)
    cols = get_columnCount(A)

    if type(rows) == int and type(cols) == int:
        if rows == 0:
            return 'Error (get_element): invalid input matrix'
        
        if rows <= i or cols <= j:
            return 'Error (get_element): invalid element position'
    
        return A[i][j]

    return 'Error (get_element): invalid input matrix'

#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (int)
# Return:       matrix
# Description:  Create an empty matrix of size r x c
#               All elements are initialized to integer pad
# Error:        r and c should be positive integers
#               (except the following which is valid 0x0 --> [])
#                   return 'Error (new_matrix): invalid size'
#               pad should be an integer
#                   return 'Error (new_matrix): invalid pad'
#-----------------------------------------------------------
def new_matrix(r,c,pad):
    if type(r) != int or type(c) != int:
        return 'Error (new_matrix): invalid size'

    if type(pad) != int:
        return 'Error (new_matrix): invalid pad'
    
    if r < 0 or c < 0 or (r == 0 and c > 0):
        return 'Error (new_matrix): invalid size'
    
    if r == 1:
        return [pad for i in range(c)] 

    return [[pad for i in range(c)] for j in range(r)]

#-----------------------------------------------------------
# Parameters:   size (int)
# Return:       square matrix (identity matrix)
# Description:  returns the identity matrix of size: [size x size]
# Examples:     0 --> Error
#               1 --> [1]
#               2 --> [[1,0],[0,1]]
# Errors        size should be a positive integer
#                   return 'Error (get_I): invalid size'
#-----------------------------------------------------------
def get_I(size):
    if size == 1:
        return [1]

    if size > 1:
        matrix = new_matrix(size, size, 0)
        matrix[0][0] = 1

        for i in range(size):
            for j in range(size):
                if i == j:
                    matrix[i][j] = 1
        
        return matrix
    
    return 'Error (get_I): invalid size'

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid identity matrix
#-----------------------------------------------------------
def is_identity(A):
    if is_square(A):
        if type(A) is not list:
            return False
        
        if type(A[0]) is not list:
            if A[0] == 1:
                return True
            
            return False
        
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j and A[i][j] != 0:
                    return False
                
                elif i == j and A[i][j] != 1:
                    return False
        
        return True
            
    return False

#-----------------------------------------------------------
# Parameters:   c (int)
#               A (matrix)
# Return:       a new matrix which is the result of cA
# Description:  Performs scalar multiplication of constant c with matrix A
# Errors:       if A is empty or not a valid matrix or c is not an inger:
#                   return 'Error(scalar_mul): invalid input'
#-----------------------------------------------------------
def scalar_mul(c,A):
    size = get_size(A)
    matrix = new_matrix(size[0], size[1], 0)

    if len(A) == 0:
            return 'Error(scalar_mul): invalid input'

    if is_square(A) and type(c) is int:
        for i in range(get_rowCount(A)):
            for j in range(get_columnCount(A)):
                matrix[i][j] = A[i][j] * 10

        return matrix

    if is_vector(A) and type(c) is int:
        for i in range(get_columnCount(A)):
            matrix[i] = A[i] * 10

        return matrix

    return 'Error(scalar_mul): invalid input'

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               B (matrix)
# Return:       a new matrix which is the result of AxB
# Description:  Performs cross multiplication of matrix A and matrix B
# Errors:       if eithr A or B or both is empty matrix nor not a valid matrix
#                   return 'Error(mul): invalid input'
#               if size mismatch:
#                   return 'Error(mul): size mismatch'
#-----------------------------------------------------------
def mul(A,B):
    if len(A) == 0 and len(B) == 0:
        return 'Error(mul): invalid input'
    
    if not is_matrix(A) or not is_matrix(B):
        return 'Error(mul): invalid input'
    
    sizeA = get_size(A)
    sizeB = get_size(B)

    if sizeA[1] != sizeB[0]:
        return 'Error(mul): size mismatch'
    
    matrix = new_matrix(sizeA[0], sizeB[1], 0)

    if is_vector(A) and is_vector(B):
        for i in range(len(A)):
            for j in range(len(B)):
                matrix[i] += A[i] * B[j]

        return matrix

    if is_vector(A) and is_matrix(B):
        for i in range(sizeA[1]):
            for j in range(sizeB[1]):
                matrix[j] += A[i] * B[i][j]
        
        return matrix

    if is_matrix(A) and is_matrix(B):
        for i in range(sizeA[0]):
            for j in range(sizeB[1]):
                for k in range(sizeB[0]):
                    matrix[i][j] += A[i][k] * B[k][j]

    return matrix

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       A` (matrix)
# Description:  Returns matrix A such that each element is the 
#               residue value in mode m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(matrix_mod): invalid input'
#               if m is not a positive integer:
#                   return 'Error(matrix_mod): invalid mod'
#-----------------------------------------------------------
def matrix_mod(A,m):
    size = get_size(A)
    matrix = new_matrix(size[0], size[1], 0)

    if is_matrix(A):
        if m > 0 and len(A) > 0:
            if type(A[0]) is list:
                for i in range(get_rowCount(A)):
                    for j in range(get_columnCount(A)):
                        matrix[i][j] = A[i][j] % m

            else:
                for i in range(get_columnCount(A)):
                    matrix[i] = A[i] % m
            
            return matrix
        
        return 'Error(matrix_mod): invalid mod'
    
    return 'Error(matrix_mod): invalid input'

#-----------------------------------------------------------
# Parameters:   A (matrix)
# Return:       determinant of matrix A (int)
# Description:  Returns the determinant of a 2x2 matrix
# Errors:       if A is empty matrix nor not a valid square matrix
#                   return 'Error(det): invalid input'
#               if A is square matrix of size other than 2x2
#                   return 'Error(det): Unsupported matrix size'
#-----------------------------------------------------------
def det(A):
    if not is_matrix(A):
        return 'Error(det): invalid input'

    elif len(A) != 2 or len(A[0]) != 2:
        return 'Error(det): Unsupported matrix size'

    return A[1][1] * A[0][0] - A[1][0] * A[0][1]

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       a new matrix which is the inverse of A mode m
# Description:  Returns the inverse of a 2x2 matrix in mode m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(inverse): invalid input'
#               if A is not a square matrix or a matrix of 2x2 with no inverse:
#                   return 'Error(inverse): matrix is not invertible'
#               if A is a square matrix of size other than 2x2
#                   return 'Error(inverse): Unsupported matrix size'
#               if m is not a positive integer:
#                   return 'Error(inverse): invalid mod'
#-----------------------------------------------------------
def inverse(A,m):
    size = get_size(A)
    d = det(A)

    if not is_matrix(A):
        return 'Error(inverse): invalid input'

    elif size[0] < 2 or not mod.has_mul_inv(d, m):
        return 'Error(inverse): matrix is not invertible'

    elif size[0] != 2 and size[1] != 2:
        return 'Error(inverse): Unsupported matrix size'
    
    elif m < 1:
        return 'Error(inverse): invalid mod'
    
    d = mod.mul_inv(d % m, m)
    inverse = new_matrix(size[0], size[1], 0)
    inverse[0][0] = A[1][1]
    inverse[0][1] = -A[0][1]
    inverse[1][0] = -A[1][0]
    inverse[1][1] = A[0][0]
    
    for i in range(2):
        for j in range(2):
            inverse[i][j] %= m
            inverse[i][j] *= d
            inverse[i][j] %= m
            
    return inverse
