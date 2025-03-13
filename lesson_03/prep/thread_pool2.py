import concurrent.futures
import time
import math

def calculate_factorial(n):
    return math.factorial(n)

# Create a large array of values
numbers = [5, 10, 15, 20, 25, 30, 35, 40] * 10000

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(calculate_factorial, numbers))

end_time = time.time()

# Sequential version for comparison
start_time_sequential = time.time()
results_sequential = [calculate_factorial(n) for n in numbers]
end_time_sequential = time.time()

print()
print(f"Time taken (with thread pool): {end_time - start_time:.4f} seconds")
print(f"Time taken (sequential): {end_time_sequential - start_time_sequential:.4f} seconds")
