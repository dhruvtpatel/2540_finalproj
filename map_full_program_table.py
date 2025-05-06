mapping = {
    'function_11': 'random_mod_calculator',
    'function_12': 'digit_sum_processor',
    'function_13': 'random_value_adjuster',
    'function_14': 'ceiling_multiplier',
    'function_15': 'factorial_root_calculator',
    'function_16': 'digit_length_scorer',
    'function_17': 'random_double_modulo',
    'function_18': 'modulo_scaler',
    'function_19': 'random_adjustment_calculator',
    'function_20': 'factorial_mod_processor',
    'function_21': 'modular_doubler',
    'function_22': 'ceiling_adjustment_calculator',
    'function_23': 'random_sequence_generator',
    'function_24': 'digit_sum_multiplier',
    'function_25': 'factorial_square_root_mod',
    'function_26': 'decimal_ceiling_adjuster',
    'function_27': 'modular_scaling_calculator',
    'function_28': 'digit_count_processor',
    'function_29': 'random_mod_adjuster',
    'function_30': 'factorial_root_modulo',
    'function_31': 'random_pair_modulo',
    'function_32': 'digit_pair_calculator',
    'function_33': 'modular_multiplication_scaler',
    'function_34': 'float_ceiling_adjuster',
    'function_35': 'factorial_modulo_processor',
}
input_path = '/Users/sohamgupta/Downloads/full_program_table.tex'
output_path = '/Users/sohamgupta/Downloads/full_program_table_mapped.tex'
with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
    for line in fin:
        for k, v in mapping.items():
            line = line.replace(k, v)
        fout.write(line) 