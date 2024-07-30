list1 = list()  # new, empty list
fruits = ['apple', 'banana', 'mango']
list2 = []  # empty list
more_fruits = "tangerine pineapple grape".split()

print(f"{list1 = }")
print(f"{fruits = }")
print(f"{list2 = }")
print(f"{more_fruits = }")

cities = ['Houston', 'Tucson', 'Woodbridge']
print(f"{cities = }\n")

cities.append('Durham')
print(f"{cities = }\n")

cities.append("Pittsburgh")
print(f"{cities = }\n")

cities.insert(0, "Los Angeles")
cities.insert(3, "Boston")
print(f"{cities = }\n")

more_cities = ["Tampa", "Norfolk", "Annapolis", "Harrisburg"]
cities.extend(more_cities)
print(f"{cities = }\n")

#  LIST.append(obj)  LIST.insert(pos, obj) LIST.extend(iterable)

cities[2] = "Tempe"

print(f"{cities = }\n")

del cities[3]
print(f"{cities = }\n")

city = cities.pop()
print(f"{city = }")
print(f"{cities = }\n")

city = cities.pop(0)
print(f"{city = }")
print(f"{cities = }\n")

cities.remove('Tampa')
print(f"{cities = }\n")

print(f"{len(cities) = }")

print(f"{cities[0] = }")
print(f"{cities[4] = }")
print(f"{cities[6] = }")

print(f"{cities[-1] = }")  # len(cities) - 1

print(f"{cities = }\n")

#    start-at:stop-before:count-by
#    start-at:stop-before
#    start-at:     go to end
#    :stop-before  start at beginning

print(f"{cities[2:6] = }\n")
print(f"{cities[2:5] = }\n")
print(f"{cities[0:3] = }\n")
print(f"{cities[:3] = }\n")
print(f"{cities[-2:] = }\n")

person = "Bob Newhart"
print(f"{person[4:7] = }\n")
print(f"{person[-4:] = }\n")
print(f"{person[:3] = }\n")

print(f"{cities = }\n")

for city in cities:
    print(city.upper())
print()

#  for VAR in ITERABLE:
#     ...

#     unpacked!
#  for VAR1, VAR2, ... in ITERABLE:
#     ...

for character in person:
    print(character)
print()

print(f"{cities = }\n")

print(f"{'Durham' in cities = }\n")
print(f"{'San Francisco' in cities = }\n")

print('-' * 60)
print(f"{[True] * 10 = }")

data = [0] * 25
print(f"{data = }\n")

print(f"{len(cities) = }\n")

print(f"{min(cities) = }")
print(f"{max(cities) = }")
print(f"{sorted(cities) = }")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

total = sum(nums)
print(f"{total = }")

print(f"{cities = }\n")

rev_cities = reversed(cities)
print(f"{rev_cities = }")

for city in rev_cities:
    print(city)
print()

a = ['a', 'b', 'c']
b = [1, 2, 3]
c = zip(a, b)
print(f"{c = }")
for x in c:
    print(x)
print()

combo = list(zip(a, b))
print(f"{combo = }\n")

for i, city in enumerate(cities):
    print(i, city)
print()

print(f"{list(enumerate(cities)) = }\n")

for i in range(5):
    print("python is great!")
print()

# range(start-at, stop-before)
# range(stop-before)
# range(start-at, stop-before, count-by)

for i in range(1, 11):
    print(i)
print()




