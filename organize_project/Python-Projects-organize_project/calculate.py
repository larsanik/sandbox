from power.power_calculate import calculate_power
from sqrt.sqrt_calculate import calculation_sqrt


def calculate_vector_length(x, y):
    value = calculate_power(x, 2) + calculate_power(y, 2)
    result = calculation_sqrt(value)
    
    return result


print(calculate_vector_length(2, 2))
