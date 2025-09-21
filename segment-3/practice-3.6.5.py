rectangle_a_side, rectangle_b_side = int(input()), int(input())
triangle_side, triangle_height = int(input()), int(input())
circle_radius, pi = int(input()), 3.14

rectangle_area = float(rectangle_a_side * rectangle_b_side)
triangle_area = 0.5 * triangle_side * triangle_height
circle_area = pi * circle_radius ** 2

print(rectangle_area)
print(triangle_area)
print(circle_area)
