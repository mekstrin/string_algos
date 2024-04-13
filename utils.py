from pathlib import Path
from functools import wraps
from time import time

BAD_TESTS_PREFIX = "bad_"
GOOD_TESTS_PREFIX = "good_"

NUMBER_OF_STARTS = 10


def get_file_content(file: Path) -> str:
    with file.open(mode="r") as file_fd:
        return file_fd.read()


def get_tests() -> dict[str, tuple[str, str]]:
    result = dict()
    benchmarks_dir = Path(__file__).parent / "benchmarks"
    for i in range(1, 5):
        result[f"{BAD_TESTS_PREFIX}{i}"] = (get_file_content(benchmarks_dir / f"{BAD_TESTS_PREFIX}t_{i}.txt"),
                                            get_file_content(benchmarks_dir / f"{BAD_TESTS_PREFIX}w_{i}.txt"))
        result[f"{GOOD_TESTS_PREFIX}{i}"] = (get_file_content(benchmarks_dir / f"{GOOD_TESTS_PREFIX}t_{i}.txt"),
                                             get_file_content(benchmarks_dir / f"{GOOD_TESTS_PREFIX}w_{i}.txt"))
    return result


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        results = []
        for _ in range(NUMBER_OF_STARTS):
            start = time()
            result = f(*args, **kw)
            end = time()
            results.append(end - start)
        return result, sum(results) / len(results)

    return wrap
