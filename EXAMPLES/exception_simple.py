
try:  # Execute code that might have a problem
    x = 5
    y = "cheese"
    m = x / 0
    z = x + y
    print("Bottom of try")

# except error-type as variable:
except (TypeError, ZeroDivisionError) as err:    # Catch the expected error; assign error object to err
    print("Naughty programmer! ", err)
except Exception as err:
    print("Did not expect:", err)

print("After try-except")  # Get here whether or not exception occurred
