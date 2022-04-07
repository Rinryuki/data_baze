import pickle
class Stud:
    fam = None
    name = None
    nom = None
    dr = None
f=open('Friends.txt','r',encoding='utf-8')
ST=[]
while True:
    x=f.readline()
    if not x:
        break
    x=x.split()
    st=Stud()
    st.fam = x[0]
    st.name = x[1]
    st.nom = x[2]
    st.dr=list(map(int,x[3].split('.')))
    ST.append(st)
fout=open('Friends.dat','wb')
pickle.dump(ST,fout)
fout.close()
f.close()
