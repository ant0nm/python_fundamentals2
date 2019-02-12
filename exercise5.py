# define the temperature converter (Fahrenheit to Celsius)
def FtoC(tempFahrenheit):
    tempCelsius = (tempFahrenheit - 32) * (5/9)
    return tempCelsius

# prompt the user for a temperature in Fahrenheit
print("Hi user, please provide the Fahrenheit temperature to be converted to Celsius:")
user_input = input()
tempF = int(user_input)
tempC = FtoC(tempF)
print("{:.2f} Fahrenheit is {:.2f} in Celsius".format(tempF, tempC))
