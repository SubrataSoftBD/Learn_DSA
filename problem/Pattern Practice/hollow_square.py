def hollow_square(n: int) -> list[str]:
    result = []
    for i in range(n):
        if i == 0 or i == n - 1:
            result.append("*" * n)
        else:
            row = "*" + " " * (n - 2) + "*"
            result.append(row)
    return result

# for i in hollow_square(10):
#     print(i)

print(hollow_square(10))