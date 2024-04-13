from utils import timing


@timing
def naive_algo(text: str, pattern: str) -> tuple[list[int], int]:
    result = []
    op_num = 0

    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            op_num += 1
            if text[i + j] != pattern[j]:
                break
        else:
            result.append(i)
    return result, op_num
