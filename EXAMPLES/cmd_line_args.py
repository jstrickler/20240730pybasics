
import sys   # Import the sys module 

print(sys.argv) # Print all parameters, including script itself

if len(sys.argv) < 2:
    print("please provide argument(s)")
    sys.exit()  # exit program


name = sys.argv[1]  # Get the first actual parameter
print("name is", name)
