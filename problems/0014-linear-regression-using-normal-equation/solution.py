import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]: #inputs
#saying


    # Your code here, make sure to round
    #numpy arrays for calculations
    X = np.array(X)
    y = np.array(y) #vector is a matrix, just bx1
    #once we have x,y we need linear regression to learn mx+b. mx is the dot product

    #from copilot
    theta = (np.linalg.inv(X.T @ X) @ X.T @ y).round(4)
    return theta.tolist() #to match the return type