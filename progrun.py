# -*- coding: utf-8 -*-

from PIL import Image as img
import numpy as np
import time
import RPi.GPIO as GPIO

im1=img.open("C:/Users/SIMPLYCASH/Pictures/Saved Pictures/image0.png")

def testpixel(p,r,g,b,a,t):     #Renvoie un si le pixel p correspond à la couleur du pixel cible
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


def imtomat(im,r,g,b,a,t):  #à partir d'une image renvoie une matrice dont le l'élément (0,0) correspond au pixel supérieur gauche de l'image
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
                posi.append((i,j))  #on récupère la liste des postions non nulles de la matrice
    return (matest,posi)
     

def lignedroite(p,mat,g):   #ajoute à la liste g les pixels à droite et sur la même ligne que le pixel p ayant la couleur cible 
    (x,y)=mat.shape
    (i,j)=p
    while j<y-2:
        if mat[i][j]:
            mat[i][j]=0
            g.append((i,j))
            j+=1
        else:
            break  #dès qu'il n'y a plus de voisin ayant la bonne couleur on s'arrête
    return g
    
def lignegauche(p,mat,g):   #idem que lignedroite pour les pixels à gauche
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
    for k in np.linspace(i+1,x-2,1,dtype=int):
        if mat[k][j]:
            l=l+chercheligne((k,j),mat)
        else:
            break
    return l


def groupement(m,posi):     #Renvoie un liste de liste contenant des pixels de la bonne couleurs tous voisins entre eux
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
        (y,x)=p                 #m[i][j] correspond au pixel ayant la possition (j,i) dans le plan (le point (0,0) étant le pixel dans le coin en haut à gauche)
        xmoy=xmoy+x*x
        ymoy=ymoy+y*y
        n+=1.                   # 1. pour avoir n de type float
    xmoy=(1/n)*np.sqrt(xmoy)
    ymoy=(1/n)*np.sqrt(ymoy)
    return (xmoy,ymoy)
    
def indmaxlen(gr): #Renvoie l'indice de la liste ayant le plus d'éléments
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


def retour(cible,x,l):      #Calcule la couleur moyenne des pixels identifiés comme étant la cible
    n=len(cible)
    rmoy=0
    gmoy=0
    bmoy=0
    for p in cible:
        (i,j)=p
        (r,g,b,a)=l[int(x)*i+j]
        rmoy+=r
        gmoy+=g
        bmoy+=b
    return (rmoy/n,gmoy/n,bmoy/n)

pin=(12,16,19,6,20,26)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

Frwd=(1,1,0,1,1,0)
Rvrs=(1,0,1,1,0,1)
Lft=(0,0,0,1,1,0)
Rgt=(1,1,0,0,0,0)
Stp=(1,0,0,1,0,0)
Free=(0,0,0,0,0,0)

def forward(x):     #fait avancer la voiture durant un temps x
    GPIO.output(pin,Frwd)
    time.sleep(x)
    GPIO.output(pin,Free)
    
def reverse(x):     #fait reculer la voiture durant un temps x
    GPIO.output(pin,Rvrs)
    time.sleep(x)
    GPIO.output(pin,Free)
    
def left(x):        #fait avancer la voiture vers la gauche durant un temps x
    GPIO.output(pin,Lft)
    time.sleep(x)
    GPIO.output(pin,Free)
def right(x):       #fait avancer la voiture vers la droite durant un temps x
    GPIO.output(pin,Rgt)    
    time.sleep(x)
    GPIO.output(pin,Free)
    
def stop(x):        #arrête la voiture
    GPIO.output(pin,Stp)
    time.sleep(x)
    GPIO.output(pin,Free)

while 1:
    im1=img.open
    (m,pos)=imtomat(im1,r,g,b,a,t)
    gr=groupement(m,pos)            
    if gr==[]:
        stop()
    else:
        cible=gr[indmaxlen(gr)]
        (x,y)=posmoy(cible)
        (r,g,b)=retour(cible,1680,list(im1.getdata())
        if x<1340 :
            left(5)
        else:
            right(5)
    