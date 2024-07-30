airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
print(f"{airports = }\n")

print(f"{airports.keys() = }\n")

print(f"{airports.values() = }\n")

print(f"{airports['MCO'] = }\n")

print(f"{airports['RDU'] = }\n")

# print(f"{airports['IAH'] = }\n")
print(f"{airports.get('IAH') = }\n")
print(f"{airports.get('IAH', 'NOT FOUND') = }\n")
print(f"{airports.get('RDU') = }\n")

for key in 'SJU', 'YOW', 'PGH', 'MCI', 'MIL':
    print(f"is {key} in dict? {key in airports}")
print()
print('-' * 60)

#   key, value
for code, city in airports.items():
    print(code, city)
