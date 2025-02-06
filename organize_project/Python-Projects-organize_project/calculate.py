import my_math.power_calculate as power_calculate
import my_math.sqrt_calculate as sqrt_calculate


def calculate_vector_length(x, y):
    value = power_calculate.calculate_power(x, 2) + power_calculate.calculate_power(y, 2)
    result = sqrt_calculate.calculation_sqrt(value)
    
    return result


print(calculate_vector_length(2, 2))
