# print(int('label')^13)
result = [ord(x) ^ 13 for x in 'label']
print (result)
print ("".join(chr(x) for x in result))


