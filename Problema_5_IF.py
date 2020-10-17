zn=int(input('Introduceti ziua nasterii='))
ln=int(input('Introduceti luna nasterii='))
an=int(input('Introduceti anul nasterii='))
zc=int(input('Introduceti ziua curenta'))
lc=int(input('Introduceti luna curenta'))
ac=int(input('Introduceti anul curent'))
if (lc>ln):
    print((ac-an),'ani')
if (lc==ln) and (zc==zn):
    print((ac-an)-1,'ani')
if (lc<ln):
    print((ac-an)-1,'ani')
else:
    print('Eroare')