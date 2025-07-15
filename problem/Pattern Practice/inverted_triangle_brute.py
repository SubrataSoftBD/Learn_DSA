def inverted_triangle_brute(n : int):
    result = []
    for i in range(n, 0, -1):
        row = "*" * i
        result.append(row)
    return result

print(inverted_triangle_brute(5))

for line in inverted_triangle_brute(5):
    print(line)