def find_square_roots(p, ints):
    roots = {}
    
    for x in ints:
        found = False
        for a in range(1, p):
            if (a * a) % p == x:
                roots[x] = a
                found = True
                break
        if not found:
            roots[x] = None
    
    return roots

# Input: p = 29, ints = [14, 6, 11]
p = 29
ints = [14, 6, 11]

# Tìm các quadratic residue và square root của chúng
roots = find_square_roots(p, ints)

# In kết quả
for x, root in roots.items():
    if root is not None:
        print(f"Quadratic Residue: {x}, Square Root: {root}")

