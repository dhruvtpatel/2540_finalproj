import math
import datetime


def calculate_discount_transformed(price: float, discount_rate: float):
    '''
    pre: 0 <= price <= 1000
    pre: 0 <= discount_rate <= 1
    post: (abs(price - 100) < 0.001 and abs(discount_rate - 0.5) < 0.001) == (round(price * (1 - discount_rate)) == 50)
    '''
    b_early = (abs(price - 100) < 0.001 and abs(discount_rate - 0.5) < 0.001)
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    b_final = (rounded_price == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_price
