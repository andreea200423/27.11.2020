from fractions import Fraction
a=int(input("Numaratorul 1 fractii: "))
b=int(input("Numitorul 1 fractii: "))
c=int(input("Numaratorul a 2 fractii: "))
d=int(input("Numitorul 2 fractii: "))
s=Fraction(a,b) + Fraction(c,d)
p=Fraction(a,b) + Fraction(c,d)
print(f"a) suma e {s}, b) produsul e {p}")