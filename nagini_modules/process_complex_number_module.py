import math

def process_complex_number_transformed(real: float, imag: float) -> int:
    '''
    pre: -1000 <= real <= 1000  # Add reasonable bounds for real part
    pre: -1000 <= imag <= 1000  # Add reasonable bounds for imaginary part
    post: (int(math.sqrt(real**2 + imag**2) + 0.5) == 10) == b_early
    '''
    # Use Pythagoras instead of complex number
    b_early: bool = int(math.sqrt(real**2 + imag**2) + 0.5) == 10
    
    # Calculate magnitude manually instead of using complex numbers
    magnitude: float = math.sqrt(real**2 + imag**2)
    rounded_magnitude: int = int(magnitude + 0.5)  # Manual rounding
    
    b_final: bool = (rounded_magnitude == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_magnitude 