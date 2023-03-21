def area_of_sphere(num):
    pi = 3.142
    surf_area = 4 * pi * (num ** 2)
    return f"The Surface Area of radius {num} is {surf_area}"

print(area_of_sphere(int(input("Enter your radius value: "))))