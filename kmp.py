from utils import timing


def prefix_function(text: str) -> tuple[list[int], int]:
    op_num = 0
    prefix_array = [0] * len(text)
    prefix_array[0] = 0
    for i in range(1, len(text)):
        prefix_function_prev_value = prefix_array[i - 1]
        while prefix_function_prev_value > 0 and text[i] != text[prefix_function_prev_value]:
            prefix_function_prev_value = prefix_array[prefix_function_prev_value - 1]
        if text[i] == text[prefix_function_prev_value]:
            prefix_function_prev_value += 1
        op_num += 2
        prefix_array[i] = prefix_function_prev_value
    return prefix_array, op_num


@timing
def kmp(text: str, pattern: str) -> tuple[list[int], int]:
    result = []
    text_pattern_contact = f"{pattern}#{text}"
    prefix_array, op_num = prefix_function(text_pattern_contact)
    for i in range(len(text)):
        op_num += 1
        if prefix_array[i + len(pattern) + 1] == len(pattern):
            result.append(i - len(pattern) + 1)

    return result, op_num
