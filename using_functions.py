def hello():
    print("Hello!")

hello()  # call the function
print()

def double(x):
    return x * 2

print(f"{double(6) = }")
print(f"{double('spam') = }")
print(f"{double(0.0) = }")

result = double("trouble")
print(f"{result = }")

m = hello()
print(f"{m = }")

def greet(whom="world"):  # default argument
    print(f"Hello, {whom}")



greet('world')
greet('Mom')
greet("it's me")
greet()
