r = 84  #radius of circular pond in metres

# Formula of area of circle is 
a = 3.14 * r**2   #area of circular pond

print(f"The area of the pond is {a} square metre")

water_per_squaremetre = 1.4
total_water = int(a*water_per_squaremetre)

print(f"The total amount of water in the pond is {total_water} L")

