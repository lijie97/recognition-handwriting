from functools import reduce

xmax=300
xmin=-300
ymax=300
ymin=-300
L=[]
ch='1'
f=open(ch+'.sav','r')
n=int(f.readline())
for i in range(n):
    m=int(f.readline())
    l=[]
    for j in range(12):
            l.append([])
            for k in range(12):
                l[j].append(0)
    for i in range(m):
        x=int(f.readline())
        y=int(f.readline())
        #如果划分成9格
        l[(x+300)//50][(y+300)//50]+=1
    L.append(reduce(list.__add__,l))

L=list(zip(*L))
rslt=[sum(L[i])/len(L[i]) for i in range(len(L))]
#print(rslt)
f.close()

f=open(ch+'.dat','w')
for i in range(len(rslt)):
    f.write(str(rslt[i])+"\n")
f.close()
