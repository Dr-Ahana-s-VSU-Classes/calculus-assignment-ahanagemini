import numpy as np
from lab7 import loss_function, compute_gradient_manual

def gradient_descent(start_w1, start_w2, alpha, num_iterations):
    """Instructor solution implementation for Task 1"""
    w = np.array([float(start_w1), float(start_w2)])
    weight_history = [w.copy()]
    loss_history = [loss_function(w[0], w[1])]
    
    for _ in range(num_iterations):
        grad = compute_gradient_manual(w[0], w[1])
        
        # Complete vector update step applying step values dynamically
        w = w - alpha * grad
        
        weight_history.append(w.copy())
        loss_history.append(loss_function(w[0], w[1]))
        
    return np.array(weight_history), np.array(loss_history)
