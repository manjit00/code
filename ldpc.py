import numpy as np
from pyldpc import make_ldpc, encode, decode, get_message

n = 15
d_v = 4
d_c = 5
snr = 20

H, G = make_ldpc(n, d_v, d_c, systematic=True, sparse=True)
#print (H)
#print (G)
k = G.shape[1]
#print (k)
data = np.random.randint(2,size=k)
print (data)
y = encode(G,data,snr)
print(y)
d = decode(H,y,snr)
print(d)
x = get_message(G,d)
print(x)