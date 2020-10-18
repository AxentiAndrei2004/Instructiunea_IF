xa=int(input('Bile albe mici='))
xr=int(input('Bile rosii mici='))
xv=int(input('Bile verzi mici='))
ya=int(input('Bile albe mari'))
yr=int(input('Bile rosii mari'))
yv=int(input('Bile verzi mari'))
tx=xa+xr+xv
ty=ya+yr+yv
print('Suma', tx+ty)
if (xa>=0) and (ya>=0) and (xr>=0) and (yr>=0) and (xv>=0) and (yv>=0):
    if tx>ty:
         print(tx,'mici')
    if ty>tx:
         print(ty,'mari')
else:
    print('Egal')
if ((xa+ya)>(xr+yr)) and ((xa+ya)>(xv+yv)):
    print(xa+ya,'albe')
if ((xr+yr)>(xa+ya)) and ((xr+yr)>(xv+yv)):
    print(xr+yr,'rosii')
elif ((xv+yv)>(xa+ya)) and ((xv+yv)>(xr+yr)):
    print(xv+yv,'verzi')
if ((xr+yr)==(xa+ya)) and ((xr+yr)>(xv+yv)):
    print('Nr maxim de bile rosii este egal cu cel de bile albe=',xr+yr)
if ((xv+yv)==(xa+ya)) and ((xv+yv)>(xr+yr)):
    print('Nr maxim de bile albe este egal cu cel de bile verzi=',xv+yv)
if ((xr+yr)==(xv+yv)) and ((xr+yr)>(xa+ya)):
    print('Nr maxim de bile rosii este egal cu cel de bile verzi==',xr+yr)
else:
    print('Eroare')

