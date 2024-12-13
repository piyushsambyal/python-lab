def convert_temperature(temp, scale):
    if scale.lower() == 'c':
        return (temp * 9/5) + 32
    elif scale.lower() == 'f':
        return (temp - 32) * 5/9
    else:
        return "Invalid scale"

temperature = float(input("Enter the temperature: "))
scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ")

converted = convert_temperature(temperature, scale)

if scale.lower() == 'c':
    print(f"{temperature} Celsius is equal to {converted} Fahrenheit")
elif scale.lower() == 'f':
    print(f"{temperature} Fahrenheit is equal to {converted} Celsius")
else:
    print(converted)
