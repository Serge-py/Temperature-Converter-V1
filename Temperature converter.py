user_input = input("Enter the temperature in celsius: ")

try:
    celsius = float(user_input)
    fahrenheit = (celsius * 9/5) + 32

    print(f"The temperature in celsius is: {celsius}C")
    print(f"the temperature in fahrenheit is: {fahrenheit}F")

except ValueError:
    print("Error! Please enter a valid number")