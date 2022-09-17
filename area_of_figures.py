from math import pi

geometric_shape = input()
area = 0

if geometric_shape == "square":
    a = float(input())
    area = a * a
elif geometric_shape == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif geometric_shape == "circle":
    r = float(input())
    area = pi * (r ** 2)
elif geometric_shape == "triangle":
    a = float(input())
    h = float(input())
    area = 1/2 * a * h

print(f"{area:.3f}")
