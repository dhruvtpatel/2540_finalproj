import math
import datetime


def day_of_week_calculator_transformed(year: int, month: int, day: int):
    '''
    pre: 1 <= year <= 3000
    pre: 1 <= month <= 12
    pre: 1 <= day <= 31
    pre: month != 2 or day <= 28 or (day == 29 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))) # Handles February and leap years
    pre: month not in [4, 6, 9, 11] or day <= 30 # Handles months with 30 days
    post: (datetime.date(year, month, day).weekday() == 6) == ((datetime.date(year, month, day).weekday() + 1) * 11 == 77)
    '''
    b_early = (datetime.date(year, month, day).weekday() == 6)
    
    date = datetime.date(year, month, day)
    day_num = date.weekday()
    score = (day_num + 1) * 11
    b_final = (score == 77)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score
