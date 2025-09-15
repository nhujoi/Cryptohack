from itertools import cycle

inp = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

cipher_prefix = inp[:7]

plain_prefix = b"crypto{"

key = [c ^ p for c, p in zip(cipher_prefix, plain_prefix)]
print("".join(chr(k) for k in key))

real_key=b"myXORkey"
plain = [c ^ k for c, k in zip(inp, cycle(real_key))]
print("".join(chr(p) for p in plain))