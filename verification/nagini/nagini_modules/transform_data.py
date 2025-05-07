from nagini_contracts.contracts import *

@Pure
def transform_data_transformed(input_value: int) -> int:
    Requires(input_value >= 0)  # assuming a non-negative input for verification simplicity
    Ensures(Result() == (input_value * 3 + 1) // 2)
    return (input_value * 3 + 1) // 2

def caller_function(input_value: int) -> None:
    Requires(input_value >= 0)  # assuming a non-negative input for verification
    Ensures(True)  # simply ensuring absence of failure due to assertions is enough
    b_early = (input_value == 33)
    processed = transform_data_transformed(input_value)
    b_final = (processed == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"