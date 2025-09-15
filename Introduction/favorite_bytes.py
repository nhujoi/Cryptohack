key = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for k in range(256):
    decoded = bytes([b ^ k for b in key])
    text = decoded.decode()  
    if 'crypto' in text:
        print(k, text)
        break

# cách hay hơn xor key[0] và c để ra số cần tìm