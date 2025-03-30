height_of_triangle = input("Enter the height of triangle = ")
triangle_letter = []
row = 1
while row <= int(height_of_triangle):
    triangle_letter.append("$"*row)
    row += 1
print("\n".join(triangle_letter))
