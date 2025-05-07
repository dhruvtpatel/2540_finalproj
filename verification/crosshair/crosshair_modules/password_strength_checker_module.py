import math
import datetime


def password_strength_checker_transformed(password: str):
    '''
    pre: len(password) <= 50
    post: (sum([any(c.isupper() for c in password), any(c.islower() for c in password), any(c.isdigit() for c in password), any(not c.isalnum() for c in password)]) == 3) == (sum([any(c.isupper() for c in password), any(c.islower() for c in password), any(c.isdigit() for c in password), any(not c.isalnum() for c in password)]) * 25 == 75)
    '''
    b_early = (sum([any(c.isupper() for c in password), 
                   any(c.islower() for c in password),
                   any(c.isdigit() for c in password),
                   any(not c.isalnum() for c in password)]) == 3)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    strength = sum([has_upper, has_lower, has_digit, has_special]) * 25
    b_final = (strength == 75)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return strength
