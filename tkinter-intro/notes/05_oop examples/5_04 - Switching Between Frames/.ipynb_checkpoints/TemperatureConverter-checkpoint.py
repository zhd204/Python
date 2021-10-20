class TemperatureConverter:

    @staticmethod
    def f_to_c(f):
        result = (f - 32) / 1.8
        return f"{f} Fahrenheit = {result:.2f} Celsius"

    @staticmethod
    def c_to_f(c):
        result = c * 1.8 + 32
        return f"{c} Celsius = {result:.2f} Fahrenheit"
