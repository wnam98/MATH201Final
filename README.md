# Linear Algebra Final Project

## Introduction
Gaussian elimination is a method in linear algebra to solve a series of linear equations. The process involves performing a series of operations on the corresponding coefficients matrix (also known as the A matrix). Gaussian elimination can also be used to calculate the rank of a matrix, find the determinant of a matrix, and calculate the inverse of a square matrix. To perform row reduction, a series of elementary row operations must be utilized to transform the given matrix to one whose lower left corner is filled with zeros, also known as an "upper triangular" matrix. Such row operations include: swapping rows, multiplying a row by a scalar, and adding a multiple of one row to another row. The solution vector can be derived by using a process called "back-substitution", where the known variables are substituted into other equations to solve for the rest of the unknowns. A special type of reduced matrix, called reduced row echelon form, can be derived using gaussian. This matrix is an upper triangular where all the leading coefficients of the rows are equal to 1, and each column containing a leading 1 has zeros in all other entries. Transforming an augmented matrix into this form makes back-substitution unnecessary, as the modified b vector becomes equivalent to the solution vector.  

## Algorithm and Row Operations
We can apply gaussian elimination to find the solution vectors of the following example matrices. A demonstration of the row operations implemented by the algorithm are displayed below. 
<br/>
<br/>
![matrices](https://raw.github.com/wnam98/MATH201Final/master/imgs/matrices.PNG "matrices") 
<br/>
To solve the system of equations, the number of equations should be equivalent to the number of unknowns. We can express the system in matrix form, with A representing the coefficients of the unknowns, and b representing the constant terms of the equations. In reducing the coefficients matrix, the first row will be fixed, as it acts as a reference row for elimination. The elements of the first column below the first row will be transformed to zero, and the elements of the rows below the reference are multiplied by a factor. The factor is defined as the main diagonal element of the reference row divided by the first element of the corresponding row. Thus, subtracting these rows from the reference row will result in all the elements below the reference element of the first column to be equal to 0. The python algorithm traverses the matrix to perform this operation until reaching the second to last column. 
However, in case of 0 values located in the main diagonal, this algorithm implements partial pivoting to swap rows. The pivot element is defined as the first non zero element of the reference row, and determines the factor that will be multiplied to the rows that will be subtracted from the reference row. To avoid division by 0, partial pivoting involves a simple swap of the row containing a 0 pivot, with a another non-zero pivot row below it. The corresponding row in the b vector should also be swapped accordingly. This process is called "partial pivoting" because the columns are not swapped in the process.
<br/>
<br/>
![first_mat](https://raw.github.com/wnam98/MATH201Final/master/imgs/first_mat.PNG "first_mat") 
![second_mat](https://raw.github.com/wnam98/MATH201Final/master/imgs/second_mat.PNG "second_mat") 
![third_mat](https://raw.github.com/wnam98/MATH201Final/master/imgs/third_mat.PNG "third_mat") 

## Tools/Frameworks

* [Jupyter Notebook](https://jupyter.org/) - The web environment used to write the python code
* [Numpy](https://numpy.org/) - Third party framework for linear algebra/vector calculations
* [Sympy](https://www.sympy.org/en/index.html) - Python library for symbolic math and algebra

## Author

* **Walter Nam** - [profile](https://github.com/wnam98)


    

