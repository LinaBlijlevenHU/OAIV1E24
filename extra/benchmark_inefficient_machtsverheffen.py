"""
benchmark_inefficient_machtsverheffen.py

Volledig gestolen van ChatGPT om mijn eigen implementatie te testen.
"""
import time
from OAI1.machtsverheffen import vermenigvuldig, machtsverheffen

def benchmark_vermenigvuldig(a, b):
    """ Benchmark custom vermenigvuldig vs native multiplication """
    # Benchmark custom multiplication
    start_time = time.time()
    custom_result = vermenigvuldig(a, b)
    custom_time = time.time() - start_time

    # Benchmark Python's native multiplication
    start_time = time.time()
    native_result = a * b
    native_time = time.time() - start_time

    # Verify results are the same
    assert custom_result == native_result, f"Custom: {custom_result}, Native: {native_result}"

    print(f"Custom multiplication: {custom_time:.6f} seconds")
    print(f"Native multiplication: {native_time:.6f} seconds")
    print(f"Custom multiplication is {custom_time/native_time:.2f} times slower\n")

def benchmark_machtsverheffen(grondtal, exponent):
    """ Benchmark custom machtsverheffen vs native power operator """
    # Benchmark custom exponentiation
    start_time = time.time()
    custom_result = machtsverheffen(grondtal, exponent)
    custom_time = time.time() - start_time

    # Benchmark Python's native exponentiation
    start_time = time.time()
    native_result = grondtal ** exponent
    native_time = time.time() - start_time

    print(f"Custom MACHTSVERHEFFEN: {custom_time:.6f} seconds")
    print(f"Native MACHTSVERHEFFEN: {native_time:.6f} seconds")
    if native_time > 0:
        print(f"Custom MACHTSVERHEFFEN is {custom_time / native_time:.2f} times slower\n")

print("Benchmarking exponentiation by repeated multiplication (which uses repeated addition):")
benchmark_machtsverheffen(2, 1000000)