def convert_temperature(temp, unit):
    if unit == 'C':
        fahrenheit = (9/5 * temp) + 32
        kelvin = temp + 273.15
        return fahrenheit, kelvin
    elif unit == 'F':
        celsius = (5/9 * (temp - 32))
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif unit == 'K':
        celsius = temp - 273.15
        fahrenheit = (9/5 * celsius) + 32
        return celsius, fahrenheit
    else:
        return None, None


temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

# Convert temperature
converted_temp1, converted_temp2 = convert_temperature(temp, unit)

# Display results
if unit == 'C':
    print(f"The temperature in Fahrenheit is: {converted_temp1}°F")
    print(f"The temperature in Kelvin is: {converted_temp2}K")
elif unit == 'F':
    print(f"The temperature in Celsius is: {converted_temp1}°C")
    print(f"The temperature in Kelvin is: {converted_temp2}K")
elif unit == 'K':
    print(f"The temperature in Celsius is: {converted_temp1}°C")
    print(f"The temperature in Fahrenheit is: {converted_temp2}°F")
else:
    print("Invalid unit entered.")
