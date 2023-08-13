import time
import my_module

n = 30
num_runs = 1000


def cython_fibonacci(n):
    return my_module.fibonacci(n)


start_time = time.perf_counter_ns()
cython_result = 0
for _ in range(num_runs):
    cython_result = cython_fibonacci(n)
end_time = time.perf_counter_ns()

cython_time = (end_time - start_time) / num_runs

print(f"Fibonacci({n}) =", cython_result)
print(f"Cython time: {cython_time:.1f} ns")


def python_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


start_time = time.perf_counter_ns()
python_result = 0
for _ in range(num_runs):
    python_result = python_fibonacci(n)
end_time = time.perf_counter_ns()

python_time = (end_time - start_time) / num_runs

print(f"Fibonacci({n}) =", python_result)
print(f"Python time: {python_time:.1f} ns")
