# decode : byte --> string
# encode : string --> byte
def bxor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key21 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key23 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flagkey = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = bxor(key1, key21)
key3 = bxor(key2, key23)
flag23 = bxor(flagkey, key1)
flag2 = bxor(flag23, key3)
flag = bxor(flag2, key2)
print(flag.decode())