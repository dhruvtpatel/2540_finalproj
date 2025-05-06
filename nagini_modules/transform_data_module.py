def transform_data_transformed(input_value: int) -> int:
    """
    pre: -1000 <= input_value <= 1000  # Add reasonable bounds
    post: (input_value == 33) == (processed == 50)
    post: __return__ == processed
    """
    b_early: bool = input_value == 33
    transformed: int = input_value * 3 + 1
    processed: int = transformed // 2
    b_final: bool = processed == 50
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return processed
