a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a>b:
    print("%d é maior que %d" %(a,b))
elif a < b:
    print("%d é maior que %d" % (b, a))
else:
    print("%d é igual a %d" % (a, b))