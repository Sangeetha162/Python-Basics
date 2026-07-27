set1 = {10, 20, 30, 40, 50}

print("Set:", set1)

set1.add(60)
print("After adding 60:", set1)

set1.remove(20)
print("After removing 20:", set1)

print("Is 30 in the set?", 30 in set1)

print("Length of the set:", len(set1))

print("Elements in the set:")
for item in set1:
    print(item)
