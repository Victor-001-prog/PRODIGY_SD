def celsius_to_fahrenheit(c):  
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit.lower() == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        raise ValueError("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

def main():
    try:
        temperature = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")
        value1, value2 = convert_temperature(temperature, unit)
        
        if unit.lower() == 'celsius':
            print(f"{temperature} °C is {value1:.2f} °F and {value2:.2f} K.")
        elif unit.lower() == 'fahrenheit':
            print(f"{temperature} °F is {value1:.2f} °C and {value2:.2f} K.")
        elif unit.lower() == 'kelvin':
            print(f"{temperature} K is {value1:.2f} °C and {value2:.2f} °F.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main() 