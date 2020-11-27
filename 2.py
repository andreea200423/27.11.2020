sir=str(input("sir: "))
maj=0
cifr=0
cr_sp=0
for i in sir:
    if ord(i) in range (65,91):
        maj+=1
    if ord(i) in range (8,58):
        cif+=1
    if ord (i) in range(32,48) or ord(i) in range (58,65) or ord(i) in range (91,97) or ord(i) in range(123,127):
        cr_sp+=1
print(f"a) Nr de maj in sir: {maj}")
print(f"b) Nr de cifr in sir: {cifr}")
print(f"c) Nr de caract speciale in sir: {cr_sp}")