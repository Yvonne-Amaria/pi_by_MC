
import numpy as np
import time

def estimate_pi(n_samples):
    # Estimating pi using Monte Carlo sampling.
    start_time = time.time()

    # Generating random points in the square [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, n_samples)
    y = np.random.uniform(-1, 1, n_samples)

    # Calculating distances from origin
    distances_squared = x**2 + y**2

    # Counting points inside the circle (d <= 1)
    inside_circle = np.sum(distances_squared <= 1)

    # Estimating pi
    pi_estimate = 4 * inside_circle / n_samples

    elapsed_time = time.time() - start_time

    return pi_estimate, elapsed_time

def calculate_percent_error(estimate, true_value=3.14159265359):
    # Calculating percent error
    return abs((estimate - true_value) / true_value) * 100

# True value of pi
pi_value = 3.14159265359

# Sample sizes to test
sample_sizes = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]

# Print output formatting
print("Monte Carlo Estimation of π")
print("=" * 70)
print(f"True value of π: {pi_value}")
print("=" * 70)
print(f"{'Samples':<15} {'Estimated π':<15} {'Error (%)':<15} {'Time (s)':<15}")
print("-" * 70)

# Running estimation for each sample size
results = []
for n in sample_sizes:
    pi_est, elapsed = estimate_pi(n)
    error = calculate_percent_error(pi_est, pi_value)
    results.append((n, pi_est, error, elapsed))
    print(f"{n:<15} {pi_est:<15.10f} {error:<15.6f} {elapsed:<15.6f}")

print("=" * 70)
