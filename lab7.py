import numpy as np
import sympy as sp

def loss_function(w1, w2):
    return w1**2 + 3 * (w2**2)

def compute_gradient_manual(w1, w2):
    """Correct completed solution for Task 1"""
    dw1 = 2.0 * w1
    dw2 = 6.0 * w2
    return np.array([dw1, dw2])

def compute_gradient_and_critical_with_sympy():
    """Correct completed solution for Task 2"""
    # 1. Define explicit symbolic variables matching test assertions
    w1, w2 = sp.symbols('w1 w2')
    
    # 2. Declare structural loss equation
    loss_expr = w1**2 + 3 * (w2**2)
    
    # 3. Calculate analytical partial derivatives via calculus engine
    deriv_w1 = sp.diff(loss_expr, w1)
    deriv_w2 = sp.diff(loss_expr, w2)
    
    # 4. Find the values where both derivatives equal zero simultaneously
    critical_point_dict = sp.solve([deriv_w1, deriv_w2], (w1, w2))
    
    return deriv_w1, deriv_w2, critical_point_dict
