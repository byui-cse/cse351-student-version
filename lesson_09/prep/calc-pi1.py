import random
import time
import math

def estimate_pi(num_points):
    points_inside_circle = 0
    points_total = num_points

    for _ in range(points_total):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / points_total
    return pi_estimate

if __name__ == "__main__":
    total_samples = 1000000 # Increase for better accuracy

    print(f"--- Simple Monte Carlo Simulation: Estimate Pi ---")
    print(f"Using {total_samples:,} random samples...")

    start_time = time.time() # Requires 'import time' at the top
    estimated_pi = estimate_pi(total_samples)
    end_time = time.time()

    print(f"\nEstimated value of Pi: {estimated_pi}")
    print(f"Actual value of Pi:    {math.pi}")
    print(f"Difference:            {abs(math.pi - estimated_pi)}")
    print(f"Simulation took:       {end_time - start_time:.4f} seconds")
