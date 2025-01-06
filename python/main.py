import numpy as np
 
# Function to print a matrix with formatting
def print_matrix(matrix, label):
    """
    Prints the given matrix with a custom label and formatted elements.
 
    Parameters:
        matrix (numpy.ndarray): The matrix to be printed.
        label (str): A string label to describe the matrix.
 
    Exceptions:
        TypeError: Catches errors if the matrix is not valid or empty.
    """
    try:
        print('\n{}\n'.format(label))  # Print the label
        print('\n----------------------------\n')
        for row in matrix:
            # Use formatted output to display values with 3 decimal precision
            print(" ".join(f"{val:8.3f}" for val in row))  
        print('\n----------------------------\n')
    except TypeError:
        print('The matrix is empty or not correct')  # Handle invalid or empty matrices
 
 
# Function to transpose a given matrix
def transpose_matrix(matrix):
    """
    Transposes the given matrix and prints it.
 
    Parameters:
        matrix (numpy.ndarray): The matrix to be transposed.
 
    Returns:
        numpy.ndarray: The transposed matrix.
    """
    answer = matrix.T  # Transpose the matrix using numpy
    print_matrix(answer, 'Transposed matrix: ')  # Print the transposed matrix
    return answer
 
 
# Function to calculate matrix operations: addition, subtraction, or multiplication
def calculate_matrix(matrix1, matrix2, operator):
    """
    Performs matrix addition, subtraction, or multiplication based on the operator provided.
 
    Parameters:
        matrix1 (numpy.ndarray): The first matrix.
        matrix2 (numpy.ndarray): The second matrix.
        operator (str): The operation to perform ('+', '-', '*').
 
    Exceptions:
        TypeError: Handles incompatible matrix dimensions for operations.
    """
    try:
        if operator == '+':  # Perform matrix addition
            answer = np.add(matrix1, matrix2)
            print_matrix(answer, 'The sum of matrix: ')
        elif operator == '-':  # Perform matrix subtraction
            answer = np.subtract(matrix1, matrix2)
            print_matrix(answer, 'The subtraction of matrix: ')
        elif operator == '*':  # Perform matrix multiplication
            answer = np.matmul(matrix1, matrix2)
            print_matrix(answer, 'The multiplication of matrix: ')
        else:  # Handle invalid operators
            print('The operator is not correct')
    except TypeError:
        print('The dimension of matrices are not compatible')  # Handle dimension errors
 
 
# Function to fill a matrix with user input
def fill_matix(matrix):
    """
    Fills a matrix with user-provided values.
 
    Parameters:
        matrix (numpy.ndarray): The matrix to be filled.
 
    Returns:
        numpy.ndarray: The filled matrix.
    """
    for i in range(len(matrix)):  # Iterate through rows
        for j in range(len(matrix[i])):  # Iterate through columns
            # Ask user to input values for each matrix element
            val = float(input('Input the value for element i:{} j:{}'.format(i, j)))
            matrix[i][j] = val  # Set the input value to the matrix
    print_matrix(matrix, 'The matrix has been filled successfully!!!')
    return matrix
 
 
# Function to create a matrix based on user-defined dimensions
def create_matrix():
    """
    Creates a matrix of user-specified dimensions initialized with ones.
 
    Returns:
        numpy.ndarray: A newly created matrix.
    """
    # Ask the user for the number of rows and columns
    columns = int(input('Please input the number of the columns: '))
    rows = int(input('Please input the number of the rows: '))
    # Correct matrix initialization using np.ones (needs tuple for dimensions)
    matrix = np.ones((rows, columns))
    print_matrix(matrix, 'The matrix has been created successfully!!!')
    return matrix
 
 
# Main program execution block
if __name__ == "__main__":  # Incorrect condition, should be __main__
    """
    Main execution block that:
    1. Creates and fills two matrices.
    2. Performs addition, subtraction, and multiplication on the matrices.
    3. Transposes both matrices.
    """
    print("Please input the columns and rows for the first matrix")
 
    # Create and fill the first matrix
    matrix1 = fill_matix(create_matrix())
 
    print('\nPlease input the columns and rows for the second matrix\n')
 
    # Create and fill the second matrix
    matrix2 = fill_matix(create_matrix())
 
    # Perform matrix operations
    calculate_matrix(matrix1, matrix2, '+')
    calculate_matrix(matrix1, matrix2, '-')
    calculate_matrix(matrix1, matrix2, '*')
 
    # Transpose matrices
    transpose_matrix(matrix1)
    transpose_matrix(matrix2)
 