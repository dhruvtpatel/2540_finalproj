from nagini_contracts.contracts import *

def calculate_discount_transformed(price: float, discount_rate: float):
    Requires(0 <= price <= 1000  # Add reasonable price bounds)
    Requires(0 <= discount_rate <= 1  # Discount rate should be between 0 and 1)
    Ensures((price == 100 and discount_rate == 0.5) == (round(price * (1 - discount_rate)) == 50))

    pre: 0 <= price <= 1000  # Add reasonable price bounds
    pre: 0 <= discount_rate <= 1  # Discount rate should be between 0 and 1
    post: (price == 100 and discount_rate == 0.5) == (round(price * (1 - discount_rate)) == 50)
    b_early = (price == 100 and discount_rate == 0.5)
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    b_final = (rounded_price == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_price
