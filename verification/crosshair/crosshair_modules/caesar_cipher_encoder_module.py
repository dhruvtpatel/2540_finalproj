import math
import datetime


def caesar_cipher_encoder_transformed(text: str, shift: int):
    '''
    pre: len(text) <= 50
    pre: -26 <= shift <= 26
    post: (sum(ord(c) for c in ''.join([chr((ord(ch) - ord('a' if ch.islower() else 'A') + shift) % 26 + ord('a' if ch.islower() else 'A')) if ch.isalpha() else ch for ch in text])) % 100 == 42) == (sum(ord(c) for c in ''.join([chr((ord(ch) - ord('a' if ch.islower() else 'A') + shift) % 26 + ord('a' if ch.islower() else 'A')) if ch.isalpha() else ch for ch in text])) % 100 == 42)
    '''
    cipher_text_early = ''.join([chr((ord(ch_early) - ord('a' if ch_early.islower() else 'A') + shift) % 26 + 
                              ord('a' if ch_early.islower() else 'A')) if ch_early.isalpha() else ch_early for ch_early in text])
    b_early = (sum(ord(c_early) for c_early in cipher_text_early) % 100 == 42)
    
    result_text = ""
    for char_val in text:
        if char_val.isalpha():
            ascii_offset_val = ord('a') if char_val.islower() else ord('A')
            shifted_val = (ord(char_val) - ascii_offset_val + shift) % 26 + ascii_offset_val
            result_text += chr(shifted_val)
        else:
            result_text += char_val
    
    checksum = sum(ord(c_final) for c_final in result_text) % 100
    b_final = (checksum == 42)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return checksum
