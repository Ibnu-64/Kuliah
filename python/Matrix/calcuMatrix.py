import numpy as np

def matrix_sum(matrix1, matrix2):
    """
    Adds two matrices element-wise.
    
    Parameters:
    matrix1 (list of list of int/float): First matrix
    matrix2 (list of list of int/float): Second matrix
    
    Returns:
    list of list of int/float: Resultant matrix after addition
    """
    return np.add(matrix1, matrix2).tolist()

def scalar_multiply(matrix, scalar):
    """
    Multiplies a matrix by a scalar.
    
    Parameters:
    matrix (list of list of int/float): Input matrix
    scalar (int/float): Scalar value
    
    Returns:
    list of list of int/float: Resultant matrix after scalar multiplication
    """
    return np.multiply(matrix, scalar).tolist()



# Example usage:




def matrix_multiply(matrix1, matrix2):
        # """
        # Multiplies two matrices.
        
        # Parameters:
        # matrix1 (list of list of int/float): First matrix
        # matrix2 (list of list of int/float): Second matrix
        
        # Returns:
        # list of list of int/float: Resultant matrix after multiplication
        # """
    return np.dot(matrix1, matrix2).tolist()


# print("Matrix Sum:")
# print(matrix_sum(matrix1, matrix2))

# print("Scalar Multiplication:")
# print(scalar_multiply(matrix1, scalar))
def inputMatirx(rows, columns):
    matrix =[]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = int(input("Enter the element at position (" + str(i) + ", " + str(j) + "): "))
    return matrix
# print("Matrix Multiplication:")
matrix1 = inputMatirx(input("Enter the number of rows: "), input("Enter the number of columns: "))
matrix2 = inputMatirx(input("Enter the number of rows: "), input("Enter the number of columns: "))
print(matrix_multiply(matrix1, matrix2))