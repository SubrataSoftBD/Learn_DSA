def pyramid_pattern(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        row = ''
        for _ in range(n - i):
            row += ' '
        for _ in range(2 * i - 1):
            row += '*'
        for _ in range(n-i):
            row += ' '
        result.append(row)
    return result

# print(pyramid_pattern(5))
for line in pyramid_pattern(5):
    print(line)