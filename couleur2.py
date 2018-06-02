# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:21:44 2018

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

    
#l=[(1,1,1,1)]*5
#k=moyligne(l,0)

def imagetomatrice5(im,r,g,b,a,t):
    l=list(im.getdata())
    x=im.size[0]
    y=im.size[1]
    m=np.zeros((y/5,x/5),dtype=bool )       # y lignes x colonnes
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
    return (m,posi)
    
#im1=img.open("C:/Users/SIMPLYCASH/Pictures/Saved Pictures/image0.png")
#a=imagetomatrice5(im1,38,37,40,0,10)
#b=a[0]
#c=a[1]

def testpixel(p,r,g,b,a,t):
    if p[3]>a:
        a1=(r-t)<p[0]
        b1=p[0]<(r+t)
        c1=(g-t)<p[1]
        d1=p[1]<g+t
        e1=(b-t)<p[2] 
        f1=p[2]<(b+t)
        g1=a1 & b1 & c1 & d1 & e1 & f1
        return g1
    else:
        return False
        
#
#def cherchegroupe (data,r,g,b,t,a,x):
#    q=copy.deepcopy(data)
#    z=[]
#    n=0
#    for p in q:
#        if testpixel(p,r,g,b,a,t):
#            z.append([])
#            z[n].append(q.index(p))
#            q.remove(q.index(p))
#            k1=0
        
for i in range(3):
    for j in range(2):
        a12=(i,j)
        print(a12)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        