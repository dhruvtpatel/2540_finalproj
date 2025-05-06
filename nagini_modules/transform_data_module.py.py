from nagini_contracts.contracts import *

def transform_data_transformed(input_value: int):
    Requires(-1000 <= input_value <= 1000  # Add reasonable bounds)
    Ensures((input_value == 33) == ((input_value * 3 + 1) // 2 == 50))

    pre: -1000 <= input_value <= 1000  # Add reasonable bounds
    post: (input_value == 33) == ((input_value * 3 + 1) // 2 == 50)
    b_early = (input_value == 33)
    transformed = input_value * 3 + 1
    processed = transformed // 2
    b_final = (processed == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return processed
