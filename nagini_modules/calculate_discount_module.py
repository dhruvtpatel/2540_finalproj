def calculate_discount_transformed(price: float, discount_rate: float) -> int:
    """
    pre: 0 <= price <= 1000  # Add reasonable price bounds
    pre: 0 <= discount_rate <= 1  # Discount rate should be between 0 and 1
    post: (price == 100 and discount_rate == 0.5) == (int(price * (1 - discount_rate) + 0.5) == 50)
    """
    b_early: bool = price == 100 and discount_rate == 0.5
    discounted_price: float = price * (1 - discount_rate)
    # Replace round() with manual implementation
    rounded_price: int = int(discounted_price + 0.5)
    b_final: bool = rounded_price == 50
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_price
