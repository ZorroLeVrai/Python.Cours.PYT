class Temperature:
    @staticmethod
    def celsius_vers_fahrenheit(celsius):
        return celsius * 1.8 + 32
    
    @staticmethod
    def fahrenheit_vers_celsius(fahrenheit):
        return (fahrenheit - 32) / 1.8

temperature_celsius = 25
temperature_fahrenheit = Temperature.celsius_vers_fahrenheit(temperature_celsius)
print("Temperature en Fahrenheit", temperature_fahrenheit)  #77.0
