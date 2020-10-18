g=int(input('Numarul de gaini='))
b=int(input('Numarul de boabe='))
if (b//(g+1)) and (b%(g+1)==0):
    print ('Numarul de boabe primit este', int(b/(g+1)),'egalitate')
elif b/g:
    print('Curcanul Capon a primit mai mult cu', b%(g+1), 'boabe')
