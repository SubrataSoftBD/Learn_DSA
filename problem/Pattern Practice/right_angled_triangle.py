def right_angled_triangle(n : int):
    result = []
    for i in range(1, n + 1):
        row = "*" * i 
        result.append(row)
    return result
    

print(right_angled_triangle(5))