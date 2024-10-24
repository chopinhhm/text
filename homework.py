#第一题
from itertools import count
from os import remove


def add():
    a,b=map(int,input("a,b值分别为：").split())
    print(a+b)
    return a+b

add()

#第二题
a=input("随便给一个数字：")
a=list(a)
a.reverse()
if a[-1]=="-":
    a.pop(-1)
    a.insert(0,"-")
for i in a:
    print(i,end="")
print(" ")
#第三题
a=input("随便给一个数字：")
a=list(a)
for i in range(0,9):
    j=str(i)
    print(a.count(j),end="")
print(" ")
#第四题
from os.path import split

x=input("参选人数:")
x=eval(x)
b=[None]*6
c=[None]*x
d=[None]*x
e=[None]*x
f=[None]*x
h=[None]*x
k=[None]*x
p=[0]*x
u=0
for i in range(x):
    a=input(f"第{i+1}名学生信息：")
    b=a.split()
    k[i] = b[0]
    c[i] = b[1]
    d[i] = b[2]
    e[i] = b[3]
    f[i] = b[4]
    h[i] = b[5]

for i in range(x):
    if int(c[i])>80 and int(h[i])>0:
        p[i]+=8000
    if int(c[i])>85 and int(d[i])>=80:
        p[i]+=4000
    if int(c[i])>90:
        p[i]+=2000
    if int(c[i])>85 and f[i]=="Y":
        p[i]+=1000
    if int(d[i])>80 and e[i]=="Y":
        p[i]+=850
for i in range(x):
    u+=int(p[i])
o=list(enumerate(p))
o=sorted(o,key=lambda x:x[1],reverse=True)
z=int(o[0][0])
print(k[z],end=" ")
print(p[z],end=" ")
print(u)
