s1 = "spam\n"
s2 = 'spam\n'  # same!

print(f"{'pa' in s1 = }")

a = "foo"
b = "bar"
print(f"{a + b = }")

print(f"{len(a) = }")
print(f"{len(s2) = }")

person = "Taylor Swift"
print(f"{person = }")
print(f"{person.upper() = }")
p = person.upper()
print(f"{p = }")

print(f"{person.count('t') = }")
print(f"{person.count('T') = }")
print(f"{person.lower().count('t') = }")

file_name = "wombat.txt"
print(f"{file_name.endswith('.txt') = }")
print(f"{file_name.removesuffix('.txt') = }")
new_name = file_name.removesuffix('.txt') + '.pdf'
print(f"{new_name = }")

print(f"{person.find('or') = }")
print(f"{person.find('and') = }")

names = person.split()
print(f"{names = }")

annoying_person = "Jar-Jar        Binks"
names = annoying_person.split()
print(f"{names = }")

nice_person = "Bob:Newhart"
names = nice_person.split(':')
print(f"{names = }")

country = "Canada    \n"

print(f"|{country}|")
print(f"|{country.rstrip()}|")






