n1=int(input('Nr. crt primului elev='))
n2=int(input('Nr. crt celui de al doilea elev='))
n3=int(input('Nr. crt. celui de al treilea elev='))
p1=int(input('Punctajul primului elev='))
p2=int(input('Punctajul celui de al doilea elev='))
p3=int(input('punctajul celui de al treilea elev='))
if (p1>p2) and (p1>p3):
    print ('Punctajul maxim are elevul cu nr. crt.',n1)
if (p2>p1) and (p2>p3):
     print ('Punctaj maxim are elevul cu nr. crt.', n2)
if (p3>p1) and (p3>p2):
    print ('Punctaj maxim are elevul cu nr. crt.', n3)
if (p1==p2) and (p1>p3) and (p2>p3):
    print ('Punctajul maxim au elevii', n1,n2)
if (p1==p3) and (p1>p2) and (p3>p2):
    print ('Punctajul maxim au elevii',n1,n3)
if (p2>p3) and (p2>p1) and (p3>p1):
    print ('Punctajul maxim au elevii', n2,n3)