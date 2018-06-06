# -*- coding: utf-8 -*-
from PIL import Image as img
import numpy as np
import time

def testpixel(p,r,g,b,a,t):
    if p[3]>a:
        a1=(r-t)<p[0]
        b1=p[0]<(r+t)
        c1=(g-t)<p[1]
        d1=p[1]<g+t
        e1=(b-t)<p[2] 
        f1=p[2]<(b+t)
        g1=a1 & b1 & c1 & d1 & e1 & f1
    if g1 :        
        return 1
    else:
        return 0


def imtomat(im,r,g,b,a,t):
    l=list(im.getdata())
    (x,y)=im.size
    matest=np.zeros((y,x))  # y lignes x colonnes
    posi=[]
    for i in range(y):
        for j in range(x):
            p=l[x*i+j]
            a=testpixel(p,r,g,b,a,t)
            matest[i][j]=a
            if a:
                posi.append((i,j))
    return (matest,posi)
     
im1=img.open("/home/pi/Camera/image0.png")
a=time.clock()
(m,l)=imtomat(im1,50,50,50,50,50)
b=time.clock()
print(b-a)

def lignedroite(p,mat,g):       #erreur d'indices :/
    (x,y)=mat.shape
    (i,j)=p
    while j<y-2:
        if mat[i][j]:
            mat[i][j]=0
            g.append((i,j))
            j+=1
        else:
            break
    return g
    
def lignegauche(p,mat,g):   # mareche bien
    (i,j)=p
    j+=-1
    while j>0:
        if mat[i][j]:
            mat[i][j]=0
            g.append((i,j))
            j+=-1
        else:
            break
    return g

def chercheligne(p,mat):
    (x,y)=mat.shape
    (i,j)=p
    l=[]
    if j<y-2:
        if mat[i][j+1]:
            l=l+lignedroite(p,mat,[])
    if j>0:
        if mat[i][j-1]:
            l=l+lignegauche(p,mat,[])
    return l

#k1=chercheligne(l[0],m)

c=time.clock()

def cherchecolonne(p,mat):
    (x,y)=mat.shape
    (i,j)=p
    l=[]
    for k in np.linspace(i+1,x-2,1,dtype=int):
        if mat[k][j]:
            l=l+chercheligne((k,j),mat)
        else:
            break
    return l

#k2=cherchecolonne(l[0],m)

d=time.clock()

def groupement(m,posi):
    gr=[]
    for p in posi:
        g=[]
        (i,j)=p
        if m[i][j]:
            g=g+chercheligne(p,m)
        if i<m.shape[0]-2:
            if m[i+1][j]:
                g=g+cherchecolonne(p,m)
        if g<>[]:
            gr.append(g)
    return gr

k3=groupement(m,l)

e=time.clock()
print(e-d)

def posmoy(posi):
    xmoy=0
    ymoy=0
    n=0.
    for p in posi:
        (x,y)=p
        xmoy=xmoy+x*x
        ymoy=ymoy+y*y
        n+=1.                   # 1. pour avoir n de type float
    xmoy=(1/n)*np.sqrt(xmoy)
    ymoy=(1/n)*np.sqrt(ymoy)
    return (xmoy,ymoy)
    
def indmaxlen(gr):
    if gr==[]:
        return -1
    n=len(gr[0])
    i=0
    for k in range(len(gr)):
        a=len(gr[k])
        if a>n:
            n=a
            i=k
    return i

pos=posmoy(k3[indmaxlen(k3)])

print(pos)

