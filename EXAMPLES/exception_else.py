
numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    try:
        quotient = x / y
    except ZeroDivisionError as err:
        print(f"uh-oh, when x = {x} and y = {y}, {err} error")
    else:
        total += quotient  # Only if no exceptions were raised
print(total)
