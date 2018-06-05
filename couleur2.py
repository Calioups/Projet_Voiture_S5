# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 13:03:13 2018

@author: SIMPLYCASH
"""

from PIL import Image as img
import numpy as np
import copy

def moyligne5(d):
    r=0
    g=0
    b=0
    a=0
    for i in range(5):
        r+=d[i][0]
        g+=d[i][1]
        b+=d[i][2]
        a+=d[i][3]
    return(r/5.,g/5.,b/5.,a/5.)
    
def plustuple4(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1],t1[2]+t2[2],t1[3]+t2[3])

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
    
#l=[(1,1,1,1)]*5
#k=moyligne(l,0)

def imagetomatrice5(im,r,g,b,a,t):
    l=list(im.getdata())
    x=im.size[0]
    y=im.size[1]
    m=np.zeros((y/5,x/5))       # y lignes x colonnes
    posi=[]
    for i in range(y/5):
        for j in range(x/5):
            for k in range(5):
                s=(0.,0.,0.,0.)
                s=plustuple4(s,moyligne5(l[x*i+j:x*i+j+5]))
            a=testpixel(s,r,g,b,a,t)
            m[i][j]=a
            if a:
                posi.append((i,j))
    return (m,posi,l)
    
im1=img.open("C:/Users/SIMPLYCASH/Pictures/Saved Pictures/image1.png")
a=imagetomatrice5(im1,38,37,40,0,10)
b=a[0]
c=a[1]
k1=[]
    
        
    
def comptevoisin(p,mat):        
    n=0
    (x,y)=mat.shape
    (i,j)=p    
    if i>0: 
        if mat[i-1][j]>0:
            n+=1
    if i<x-2 :
        if mat[i+1][j]>0:
            n+=1
    if j>0:
        if mat[i][j-1]>0:
            n+=1
    if j<y-2:
        if mat[i][j+1]>0:
            n+=1
    return n 
    
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
    
def cherchecolonne(p,mat):
    (x,y)=mat.shape
    (i,j)=p
    l=[]
    for k in np.linspace(i+1,x-2,1):
        if k<x-2:
            if mat[k][j]:
                l=l+chercheligne((k,j),mat)
            else:
                break
    return l

def groupement(mat,posi):
    m=copy.deepcopy(mat)
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
    
def posmoy(posi):
    xmoy=0
    ymoy=0
    n=0.
    for p in posi:
        (x,y)=p
        xmoy=xmoy+x
        ymoy=ymoy+y
        n+=1.                   # 1. pour avoir n de type float
    xmoy=(1/n)*xmoy
    ymoy=(1/n)*ymoy
    return (xmoy,ymoy)
    
def indmaxlen(gr):
    if gr==[]:
        return 0
    n=len(gr[0])
    i=0
    for k in range(len(gr)):
        a=len(gr[k])
        if a>n:
            n=a
            i=k
    return i

#k3=groupement(b,c)
#pos=posmoy(k3[indmaxlen(k3)])   

def retour(cible,x,l):
    n=5*len(cible)
    rmoy=0
    gmoy=0
    bmoy=0
    for p in cible:
        (i,j)=p
        for kx in range(5):
            for ky in range(5):
                (r,g,b,a)=l[int(x)*int(i+kx)+j+ky]
                rmoy+=r
                gmoy+=g
                bmoy+=b
    return (rmoy/n,gmoy/n,bmoy/n)
            
            
def poscible(im,r,g,b,a,t):
    (m,posi,l)=imagetomatrice5(im,r,g,b,a,t)
    (x,y)=m.shape
    g=groupement(m,posi)
    cible=g[indmaxlen(g)]
    return cible,posmoy(cible),retour(cible,x,l)
  
esp=poscible(im1,38,37,40,0,10)
e1=esp[0]
e2=esp[1]  
e3=esp[2]
    