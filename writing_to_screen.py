person = "Taylor Swift"
city = "Tempe"
result = 37.248939323503

# output str(person) + " " + str(person) + " " + str(result) + "\n"
print(person, city, result)
print("next line")
print("next line")

#   red   green blue
print("red", end=" ")
# if ...
print("green", end=" ")
print("blue")

print(person, city, result, sep="/")

#  print(..., sep=" ", end="\n")

#  city: person
print(f"{city} ({person})")

#   {value:format}

print(f"{result:.2f}")

big_number = 239029352039852985

print(f"{big_number:,}")

print(f"2 + 2 is {2 + 2}")

print("city is",city)
print(f"city is {city}")
print(f"{city = }")
print(f"{city = }")

x =  f"{city = }"
print(x)

print("city is {}".format(city))  # 3.0 through 3.5

print("{} lives in {}".format(person, city))  # old way
print(f"{person} lives in {city}")  # new way







