from utils import timing

p = 101
q = 2098960


@timing
def rabin_karp(text: str, pattern: str) -> tuple[list[int], int]:
    op_num = 0
    result = list()

    h = 1
    for _ in range(len(pattern)):
        h = (h * p) % q
    hash_text = 0
    hash_pattern = 0
    for i in range(len(pattern)):
        hash_text = (ord(text[i]) + hash_text * p) % q
        hash_pattern = (ord(pattern[i]) + hash_pattern * p) % q
    for i in range(len(text) - len(pattern)):
        op_num += 1
        if hash_text == hash_pattern:  # can be hash collisions, need to check if string are really equal
            result.append(i)
        hash_text = (p * hash_text - h * ord(text[i]) + ord(text[i + len(pattern)])) % q

    op_num += 1
    if hash_text == hash_pattern:  # last value from cycle
        result.append(i + 1)

    return result, op_num
