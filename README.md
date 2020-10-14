# Syseqsolve

This program solve the system of equations given:

1. There should be as many equations as the vairables
2. The solutios are always appriximations and not the exact values


There are some functions in the program to manipulate the matrix such as


NOTE: None of them apply the modifications in place, instead a new matrix/value is created


det(matrix) 

which calculate the determinant


remove_col(matrix, row, col) 

which remove the given row and column


adjoint(matrix) 

which calculates the adjoint of the matrix



inverse(matrix) 

which calculates the inverted matrix



transpose(matrix) 


which returns the transpose of matrix




To extract the matrix out of equations:

read_eq(eq) is used


solve(matrix, rounding) is used to solve the equations

NOTE: if the determinant of matrix of variables is 0 then it will return an error even if there is a solution to it

example : 2x + 4y = 6, x + 2y = 3
