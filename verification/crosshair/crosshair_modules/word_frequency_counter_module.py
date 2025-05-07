import math
import datetime


def word_frequency_counter_transformed(text: str):
    '''
    pre: len(text) <= 200 # Increased length for more complex texts
    post: ( (lambda t: sum(1 for word in set(t.lower().split()) if t.lower().split().count(word) > 1))(text) == 3) == ( (lambda t: sum(1 for val in (lambda frq: {clean_word: frq.get(clean_word, 0) + 1 for word in t.lower().split() for clean_word in (''.join(c for c in word if c.isalpha()),) if clean_word for frq_val in (0,)})({}).values() if val > 1) * 10)(text) == 30)
    '''
    words_original = text.lower().split()
    repeats = 0
    for word_check in set(words_original):
        if words_original.count(word_check) > 1:
            repeats +=1
    b_early = (repeats == 3)
    
    freq: dict[str, int] = {}
    for word_iter in text.lower().split():
        clean_word_iter = ''.join(c for c in word_iter if c.isalpha())
        if clean_word_iter:
            freq[clean_word_iter] = freq.get(clean_word_iter, 0) + 1
    
    count = sum(1 for val_check in freq.values() if val_check > 1)
    score = count * 10
    b_final = (score == 30)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score
