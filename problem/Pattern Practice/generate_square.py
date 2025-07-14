def generate_square(n: int) -> list[str]:
    row = "*" * n
    result = []
    for _ in range(n):
        result.append(row)
    return result

print(generate_square(3))  