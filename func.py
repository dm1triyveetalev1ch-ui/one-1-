import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
def estimate_pi(num_samples, radius=1.0):  
    x = np.random.uniform(-radius, radius, num_samples)
    y = np.random.uniform(-radius, radius, num_samples)
    inside_circle = (x**2 + y**2) <= radius**2
    num_inside = np.sum(inside_circle)   
    square_area = (2 * radius) ** 2  
    estimated_area_ratio = num_inside / num_samples
    pi_estimate = estimated_area_ratio * 4
    p = num_inside / num_samples
    std_error = np.sqrt(p * (1 - p) / num_samples)

    return pi_estimate, std_error
