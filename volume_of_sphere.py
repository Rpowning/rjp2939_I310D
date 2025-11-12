def calculate_volume_of_sphere(radius):
	pi = 3.14
	volume = pi * radius ** 3 * (4/3)
	return volume

radius1 = 40
area1 = calculate_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {area1}")

radius2 = 50
area2 = compute_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {area2}")
