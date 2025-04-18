import random
import math
import multiprocessing
import time
import os

def monte_carlo_worker(num_points_to_simulate):
    points_inside = 0
    for _ in range(num_points_to_simulate):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1.0:
            points_inside += 1
    return points_inside

if __name__ == "__main__":
    total_samples = 10_000_000 # Using more samples for parallel benefit
    num_processes = os.cpu_count() or 2 # Use available cores, default to 2

    if num_processes <= 0:
        num_processes = 2

    print(f"--- Monte Carlo Pi Estimation using {num_processes} Processes ---")
    print(f"Total random samples: {total_samples:,}")

    points_per_process = total_samples // num_processes
    workload = [points_per_process] * (num_processes - 1)
    workload.append(total_samples - points_per_process * (num_processes - 1))

    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(monte_carlo_worker, workload)

    total_points_inside = sum(results)

    end_time = time.time()

    estimated_pi = 4 * total_points_inside / total_samples

    print(f"\nTotal points inside circle: {total_points_inside:,}")
    print(f"Estimated value of Pi:    {estimated_pi}")
    print(f"Actual value of Pi:       {math.pi}")
    print(f"Difference:               {abs(math.pi - estimated_pi)}")
    print(f"Simulation took:          {end_time - start_time:.4f} seconds")

