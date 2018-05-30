# -*- coding: utf-8 -*-
"""
@author: Big Lolo


"""

from PIL import Image as img
import numpy as np
import copy

#im1=img.open("image1")
#im2=img.open("image2")
#
#data1=list(im1.getdata())
#data2=list(im2.getdata())

def cherchevert(data,r,g,b,t):  #data : liste des coefficients rgb des pixels r,g,g : coefficients correspondant à la couleur de l'objet cherché t : marge d'erreur
    s=[]
    for i in range(len(data)):  #si un pixel est d'une couleur semblable à la marge près de la couleur cible on enregistre la position de ce pixel
        if (r-t)<data[i][0] & data[i][0]<(r+t) & (g-t)<data[i][1] & data[i][1]<g+t & (b-t)<data[i][2] & data[i][2]<(b+t):
            s.append(i)
    return s #retour : liste des positions

def pos(z,x):           #z : position d'un pixel    x: largeur de l'image
    return (z%x,z/x)    #retour : position (x,y) du pixel dans une représentation matricielle
    
def listepos(l,x):  #l : liste de position de pixels    x : largeur de l'image 
    s=[]
    for i in l:
        s.append(pos(i,x))
    return s    # à partir d'une liste de position dans une représentation liste on renvoie une liste de position dans une représentation matricielle
    
def comptevoisin(l,i,x):    # l :liste des positions en représentation liste   i : position d'un pixel    x,y : dimensions de l'image
    n=0                      
    if (i-1) in l:
            n+=1
    if (i+1) in l:
            n+=1
    if (i-x) in l:
            n+=1
    if (i+x) in l:
            n+=1
    return n  # retour : nombre de voisins dans une représentation matricielle

def posmoyen(l):    # l : liste de positions de pixels dans une représentation matricielle
    x=0
    y=0
    for i in range(len(l)):
        x+=l[i][0]
        y+=l[i][1]
    return (x/len(l),y/len(l)) # retour : (x,y) position moyenne des pixels
    
def suivi(data,r,g,b,t,x,y):     #data : liste des coefficients rgb des pixels r,g,g : coefficients correspondant à la couleur de l'objet cherché t : marge d'erreur x,y : position de l'image
    d=cherchevert(data,r,g,b,t)  #on regarde où sont les pixels proches de la couleur cible
    listeverte=reduction(d,x)
    position=listepos(listeverte)   
    return (posmoyen(position),listeverte) # retour (xmoy,ymoy),listepixelscibles 
    
    
def retour(data,position): # data : liste des valeurs des pixels   position : liste de la position des pixels ayant été définis comme faisant partie de la cible
    r1=0
    g1=0
    b1=0
    for i in position:
        r1+=data[i][0]
        g1+=data[i][1]
        b1+=data[i][2]
    n=len(position)
    r1=r1/n
    g1=g1/n
    b1=b1/n
    return (r1,g1,b1) #retour (r,g,b) nouvelle couleur cible
  
  
def groupe(l,i,x):
    if l==[]:
        return []
    s=[]
    if (i-1) in l:
            k=l.pop(l.index(i-1))
            s.append(k)
            s=s+groupe(l,k,x)
    if (i+1) in l:
            k=l.pop(l.index(i+1))
            s.append(k)
            s=s+groupe(l,k,x)
    if (i-x) in l:
            k=l.pop(l.index(i-x))
            s.append(k)
            s=s+groupe(l,k,x)
    if (i+x) in l:
            k=l.pop(l.index(i+x))
            s.append(k)
            s=s+groupe(l,k,x)
    return s
    
def reduction(l,x):
    s=[]    
    for a in l:         #on enlève les pixels isolés pour affiner
        if comptevoisin(l,a,x)>3:
            s.append(a)
    if len(l)<1000:
        q=copy.deepcopy(s)
        w=[]
        for a in q:
            w=w+groupe(q,a,x)
        v=[]
        for a in w:
            v.append(len(a))
        return w[w.index(max(w))]
    else :
        return s
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    