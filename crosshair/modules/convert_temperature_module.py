
def convert_temperature_transformed(celsius: float):
    '''
    pre: -100 <= celsius <= 100  # Add reasonable temperature bounds
    post: (abs(celsius - 37.7778) < 0.01) == (round(celsius * 9/5 + 32) == 100)
    '''
    b_early = abs(celsius - 37.7778) < 0.01
    fahrenheit = celsius * 9/5 + 32
    rounded_temp = round(fahrenheit)
    b_final = (rounded_temp == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_temp
