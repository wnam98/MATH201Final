# Linear Algebra Final Project

## Introduction
Gaussian elimination is a method in linear algebra to solve a series of linear equations. The process involves performing a series of operations on the corresponding coefficients matrix (also known as the A matrix). Gaussian elimination can also be used to calculate the rank of a matrix, find the determinant of a matrix, and calculate the inverse of a square matrix. To perform row reduction, a series of elementary row operations must be utilized to transform the given matrix to one whose lower left corner is filled with zeros, also known as an "upper triangular" matrix. Such row operations include: swapping rows, multiplying a row by a scalar, and adding a multiple of one row to another row. The solution vector can be derived by using a process called "back-substitution", where the known variables are substituted into other equations to solve for the rest of the unknowns. A special type of reduced matrix, called reduced row echelon form, can be derived using gaussian. This matrix is an upper triangular where all the leading coefficients of the rows are equal to 1, and each column containing a leading 1 has zeros in all other entries. Transforming an augmented matrix into this form makes back-substitution unnecessary, as the modified b vector becomes equivalent to the solution vector.  

## Algorithm and Row Operations
We can apply gaussian elimination to find the solution vectors of the following example matrices. A demonstration of the row operations implemented by the algorithm are displayed below. 
<br/>
<br/>
![matrices](https://raw.github.com/wnam98/MATH201Final/master/imgs/matrices.PNG "matrices")

    

