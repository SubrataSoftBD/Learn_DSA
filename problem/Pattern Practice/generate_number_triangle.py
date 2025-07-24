def generate_number_triangle(n):
    result = []
    for i in range(1, n+1):
        print(i)
        row = str(i) * i
        print(row)
        result.append(row)
    return result



print(generate_number_triangle(5))