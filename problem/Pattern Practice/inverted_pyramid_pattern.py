def inverted_pyramid_pattern(n: int):
    result = []
    for i in range(n):
        row = ''

        for _ in range(i):
            row +=  ' '
        for _ in range(2 * (n - i) - 1):
            row += '*'
        for _ in range(i):
            row += ' '
        result.append(row)
    return result



print(inverted_pyramid_pattern(5))