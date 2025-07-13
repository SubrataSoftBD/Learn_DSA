# import math

# def number_of_lift_rounds(n, capacity):
#     rounds = math.ceil(n / capacity)
#     return rounds


# print(number_of_lift_rounds(10, 3))


def number_of_lift_rounds(n, capacity):
    full_rounds = n // capacity
    print(f"Full Round {full_rounds}")
    print(f"Round {n % capacity}")
    if n % capacity != 0:
        return full_rounds + 1
    else:
        return full_rounds
    

print(number_of_lift_rounds(10, 3)) 