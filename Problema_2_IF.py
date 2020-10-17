a=int(input('Primul numar='))
b=int(input('Al doilea numar='))
c=int(input('Al treilea numar='))
if(a<b+c) and (b<a+c) and (c<a+b) and (a<b<c):
    print ('DA')
else:
     print('NU')