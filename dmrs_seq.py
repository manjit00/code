'DMRS sequence generation'

import numpy as np

def generate_dmrs_symbols(cell_id, slot_num):
    # DMRS configuration parameters
    n_id = cell_id % 3
    n_sc_rb = 12  # Number of subcarriers per resource block
    n_rb = 6      # Number of resource blocks
    n_sym_slot = 14  # Number of symbols per slot

    # Generate DMRS sequence
    sequence_length = n_sc_rb * n_rb
    dmrs_sequence = np.zeros(sequence_length, dtype=complex)
    print (dmrs_sequence)
    print (sequence_length)
    for n in range(sequence_length):
        q = (n // n_sc_rb) % 2
        alpha = np.exp(1j * np.pi / 6 * (2 * q * n_id + n_id * (n_id + 1) % 6))
        x = 6 * (2 * q * n_id + n_id * (n_id + 1) % 6)
        print (x)
        #print (alpha)
        dmrs_sequence[n] = alpha

    # Map DMRS symbols to the given slot
    dmrs_symbols = np.zeros(n_sym_slot, dtype=complex)
    for k in range(n_sym_slot):
        m = slot_num * n_sym_slot + k
        dmrs_symbols[k] = dmrs_sequence[m % sequence_length]

    return dmrs_symbols

# Set the cell ID and slot number
cell_id = 121
slot_num = 6

# Generate DMRS symbols
dmrs_symbols = generate_dmrs_symbols(cell_id, slot_num)

# Display the DMRS symbols
print("DMRS Symbols:")
print(dmrs_symbols)
