import numpy as np
import math

def calc_gradient_descent(math,cs):
    slope_current = intercept_current = 0
    iterations=1000000
    learning_rate=0.0002
    noofvalues = len(math)
    cost_previous = 0

    for iter in range(1,iterations):
        cs_predicted = (slope_current * math) + intercept_current
        cost = (1/noofvalues)*np.sum([val**2 for val in (cs - cs_predicted)])
        slope_derivative = -(2/noofvalues) * np.sum(math*(cs - cs_predicted))
        intercept_derivative = -(2/noofvalues) * np.sum(cs - cs_predicted)
        slope_current = slope_current - (slope_derivative*learning_rate)
        intercept_current = intercept_current - (intercept_derivative*learning_rate)

        if math.isclose(cost,cost_previous,rel_tol=1e-20):
            print(f"slope:{slope_current} ,intercept:{intercept_current}, cost:{cost} ,iteration:{iter}")
            break

        cost_previous = cost    

if __name__ == "__main__":
    math_values = np.array([92, 56, 88, 70, 80, 49, 65, 35, 66, 67])
    cs_values = np.array([98, 68, 81, 80, 83, 52, 66, 30, 68, 73])
    calc_gradient_descent(math_values,cs_values)
  
