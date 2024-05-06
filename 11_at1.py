import numpy as np

def calculate_sum(x, k):
    l = len(x)
    n = np.arange(l)
    return np.sum(x * np.cos(2 * np.pi * n * k))

x = [1, 2, 3, 4, 5]  # example array
k_values = [0, 1, 2, 3]  # example k values

for k in k_values:
    result = calculate_sum(x, k)
    print(f"For k = {k}, sum = {result}")

