def mod_exp(a, b, p):
    return pow(a, b, p)

def fermat_little_theorem(a, p):
    return mod_exp(a, p-1, p) == 1

p = int(input("Nhập số nguyên tố p: "))
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

result_exp = mod_exp(a, b, p)
print(f"{a}^{b} mod {p} = {result_exp}")

