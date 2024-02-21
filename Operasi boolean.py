# operasi logika atau boolean

# not, or, and, xor

# NOT
print('=====NOT=====')
a = False
c = not a
print('data a = ',a)
print('------------NOT')
print('data c = ',c)

# OR (|) (jika salah satu True maka hasilnya adalah True) 
# seperti operasi perjumlahan (True : 1, False : 0)
print('=====OR=====')
a = False
b = False
c = a | b
print(a,'OR',b,'=',c)
a = False
b = True
c = a | b
print(a,'OR',b,' =',c)
a = True
b = False
c = a | b
print(a,'OR',b,' =',c)
a = True
b = True
c = a | b
print(a,'OR',b,'  =',c)

# AND (&) (jika salah satu False maka hasilnya adalah False) 
# seperti operasi perkalian (True : 1, False : 0)
print('=====AND=====')
a = False
b = False
c = a & b
print(a,'AND',b,'=',c)
a = False
b = True
c = a & b
print(a,'AND',b,' =',c)
a = True
b = False
c = a & b
print(a,'AND',b,' =',c)
a = True
b = True
c = a & b
print(a,'AND',b,'  =',c)

# XOR (^) (Jika nilai nya sama, maka hasilnya False, jika nilainyaa beda, maka hasilnya True)
print('====XOR=====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'  =',c)


