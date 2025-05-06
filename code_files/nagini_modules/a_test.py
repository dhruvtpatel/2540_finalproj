# def a_test() -> int:
#     """
#     post: __return__ == 1
#     """
#     x: int = 1
#     return x


from nagini_contracts.contracts import *

# def process_data_transformed(x: int) -> int:
#     '''
#     Requires(-1000 <= x <= 1000)  # Precondition with bounds
#     Ensures(Result() == (x * 2 if x + 2 > 0 else -x * 2))  # Postcondition
#     Ensures((x == 50) == (Result() == 100))  # Assertion equivalence
#     '''
#     y = x * 2
#     z = y if y > 0 else -y
#     return z

# def transform_data_transformed(input_value: int) -> int:
#     '''
#     Requires(-1000 <= input_value <= 1000)
#     Ensures(Result() == (input_value * 3 + 1) // 2)
#     Ensures((input_value == 33) == (Result() == 50))
#     '''
#     transformed = input_value * 3 + 1
#     processed = transformed // 2
#     return processed

# def transform_data_transformed(input_value: int) -> int:
#     '''
#     Requires(-1000 <= input_value <= 1000)
#     Ensures(Result() == (input_value * 3 + 1) // 2)
#     Ensures((input_value == 33) == (Result() == 50))
#     '''
#     transformed = input_value * 3 + 1
#     processed = transformed // 2
#     return processed

# def calculate_discount_transformed(price: float, discount_rate: float) -> float:
#     '''
#     Requires(0 <= price <= 1000)
#     Requires(0 <= discount_rate <= 1)
#     Ensures(Result() == round(price * (1 - discount_rate)))
#     Ensures((price == 100 and discount_rate == 0.5) == (Result() == 50))
#     '''
#     discounted_price = price * (1 - discount_rate)
#     rounded_price = round(discounted_price)
#     return rounded_price

def add(x: int, y: int) -> int:
    Requires(x >= 0 and y >= 0)
    Ensures(Result() == x + y)
    return x + y