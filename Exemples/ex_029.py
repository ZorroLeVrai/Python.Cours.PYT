class Temperature:
    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        if name == "celsius":
            return self.value
        if name == "fahrenheit":
            return self.value * 1.8 + 32
        raise AttributeError(name)
   
    def __setattr__(self, name, value):
        if name == "celsius":
            self.value = value
        elif name == "fahrenheit":
            self.value = (value - 32) / 1.8
        else:
            super().__setattr__(name, value)

ma_temperature = Temperature(37.5)
print(ma_temperature.fahrenheit)  #99.5