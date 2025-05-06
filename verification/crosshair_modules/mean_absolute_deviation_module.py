import math
import datetime


def mean_absolute_deviation_transformed(numbers: list):
    '''
    pre: len(numbers) > 0
    pre: len(numbers) <= 20
    pre: all(-100 <= x <= 100 for x in numbers)
    post: (len(numbers) > 0 and round(sum(abs(x - sum(numbers)/len(numbers)) for x in numbers) / len(numbers) * 10) == 65) == (round(sum(abs(x - sum(numbers)/len(numbers)) for x in numbers) / len(numbers) * 10 if numbers else 0) == 65)
    '''
    b_early = len(numbers) > 0 and round(sum(abs(x - sum(numbers)/len(numbers)) for x in numbers) / len(numbers) * 10) == 65
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / len(deviations)
    result = round(mad * 10)
    b_final = (result == 65)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
