import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print ("Zadoff Chu Sequence....")
"root = root is base of the sequence and rest if all cyclically shift"
"cyclically shift makes the zadoff chu sequence orthogonal to each"
"sequence"
"N is total length of the sequence"

def generate_zadoff_chu_sequence(root,N):
    sequence = np.zeros(N,dtype=complex)
    
    for n in range(10):
        sequence[n] = np.exp(-1j*np.pi * root * n * (n +1)/N)
        
    return sequence
        
def cyclic_shift(sequence, shift):
    N = len(sequence)
    shifted_sequence = np.roll(sequence, shift)
    return shifted_sequence        

root=40
N=20

zadoff_chu_seq = generate_zadoff_chu_sequence(root,N)
print(zadoff_chu_seq)
shifted_seq = cyclic_shift(zadoff_chu_seq, 1)
print(shifted_seq)