from pprint import pprint

FILE_PATH = "DATA/knights.txt"

knight_info = {}

with open(FILE_PATH) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        data =  title, color, quest, comment   # create a tuple of the fields
        knight_info[name] = data  # assign tuple to key

pprint(knight_info)
print()

print(f"{knight_info['Gawain'] = }")
print(f"{knight_info['Gawain'][1] = }")
print(f"{knight_info['Gawain'][1][0] = }")
print()

#   key   value
#   name  tuple-of-fields
for name, info in knight_info.items():
    print(info[0], name, info[2])
print()

