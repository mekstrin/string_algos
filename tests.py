from utils import get_tests
from naive import naive_algo
from rabin_karp import rabin_karp
from kmp import kmp

tests = get_tests()
for test, (text, pattern) in tests.items():
    print(f"Test: {test}")
    (naive_algo_result, naive_algo_ops), naive_algo_time = naive_algo(text, pattern)
    (rabin_karp_algo_result, rabin_karp_algo_ops), rabin_karp_algo_time = rabin_karp(text, pattern)
    (kmp_algo_result, kmp_algo_ops), kmp_algo_time = kmp(text, pattern)
    print(f"Naive algo: result - {naive_algo_result}, "
          f"num_of_operations - {naive_algo_ops}, "
          f"time in seconds - {naive_algo_time:.{2}}.")
    print(f"Rabin karp algo: result - {rabin_karp_algo_result}, "
          f"num_of_operations - {rabin_karp_algo_ops}, "
          f"time in seconds - {rabin_karp_algo_time:.{2}}.")
    print(f"KMP algo: result - {kmp_algo_result}, "
          f"num_of_operations - {kmp_algo_ops}, "
          f"time in seconds - {kmp_algo_time:.{2}}.")
    print()
