import sys

for file_name in sys.argv[1:]:
    print(file_name)
    with open(file_name) as file_in:
        # for line in file_in:
        for i, line in enumerate(file_in):
            print(f"{i + 1:4d}: {line.rstrip()}")
    print()

