fruits = ("Apple", "Banana", "Cherry", "Mango")

print("Tuple:", fruits)
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("First two elements:", fruits[:2])
print("Length of tuple:", len(fruits))

if "Banana" in fruits:
    print("Banana is present in the tuple.")

numbers = (1, 2, 3, 2, 4, 2, 5)

print("Numbers tuple:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of Cherry:", fruits.index("Cherry"))

print("Iterating through fruits:")
for fruit in fruits:
    print(fruit)

person = ("John", 25, "Engineer")

print("Packed tuple:", person)

name, age, profession = person

print("Name:", name)
print("Age:", age)
print("Profession:", profession)

nested = (("Red", "Green"), ("Blue", "Yellow"))

print("Nested tuple:", nested)
print("First element of first tuple:", nested[0][0])

print("Program executed successfully.")
