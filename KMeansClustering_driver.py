#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:27:34 2020

@author: emeliadaro
"""
#EMMY DARO
#K MEANS CLUSTERING DRIVER
#ES-02 PROJECT 2 PART 4
#time spent: about 8 hours
#recieved help from Drew Macklin

#this is meant to be a driver file but importing the functions in was not working so 
#I have included them in the file

import KMeansClustering_functions as kmc
import numpy as np
import matplotlib.pyplot as plt
import random

# see KMeansClustering_functions for function comments
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose,hemoglobin,classification):
    glucose_scaled = []
    np.array(glucose_scaled)
    print(glucose_scaled)
    hemoglobin_scaled = []
    np.array(hemoglobin_scaled)
    for i in range(len(glucose)):
        gluc_val=(glucose[i]-70)/(490-70)
        hemo_val=(hemoglobin[i]-3.1)/(17.8-3.1)
        glucose_scaled=np.append(glucose_scaled,[gluc_val])
        hemoglobin_scaled=np.append(hemoglobin_scaled,[hemo_val])
    return glucose_scaled, hemoglobin_scaled, classification

def randomCentroid():
    return random.random()

def calculateDistanceArray(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled):
    distance_array=[]
    np.array(distance_array)
    for n in range(k):
        for i in range(len(glucose)):
            distance=np.sqrt(((glucose_scaled[i]-new_gluc)**2)+((hemoglobin_scaled[i]-new_hemo)**2))
            distance_array=np.append(distance_array,[distance])
    return distance_array

def nearestCentroid(val):
    cluster_assign=np.zeros((len(glucose)))
    for i in range(len(glucose)):
        n=np.argmin(val[i])
        cluster_assign[i]=n
    return cluster_assign

def newCentroid(val):
    gluc_total=np.zeros((k))
    hemo_total=np.zeros((k))
    gluc_avg=np.zeros((k))
    hemo_avg=np.zeros((k))
    counter=np.zeros((k))
    for i in range(len(val)):
        n=int(val[i])
        gluc_total[n]+=glucose[i]
        hemo_total[n]+=hemoglobin[i]
        counter+=1
    for n in range(len(gluc_total)):
        if counter[n]>0:
            gluc_avg[n]=gluc_total[n]/counter[n]
            hemo_avg[n]=hemo_total[n]/counter[n]
    return hemo_avg,gluc_avg
    
def updateCentroid(new_hemo,new_gluc,glucose,hemoglobin):
    for i in range(10):
        x=calculateDistanceArray(new_hemo,new_gluc,glucose,hemoglobin)
        c=nearestCentroid(x)
        new_centroid=newCentroid(c)
    return new_centroid

# initialize global variable k
k=2
#import and normalize data
glucose,hemoglobin,classification=openckdfile()
glucose,hemoglobin,classification=normalizeData(glucose,hemoglobin,classification)

new_hemo=np.zeros((k))
new_gluc=np.zeros((k))

#make k number of clusters
for i in range(k):
    new_hemo[i]=randomCentroid()
    new_gluc[i]=randomCentroid()

#call updateCEntoid to make the calculated centroids for the dataset
current_centroid=updateCentroid(new_hemo,new_gluc,glucose,hemoglobin)
centroid_number=['A']*k

#label the centroids
for j in range(k):
    centroid_number[j]=str(j+1)

#plot data and centoids using MatPlotLib
plt.plot(glucose[classification==1],hemoglobin[classification==1],'r.', label='true')
plt.plot(glucose[classification==0],hemoglobin[classification==0],'k.', label='false')
plt.xlabel('glucose!!!')
plt.ylabel('hemoglobin')
plt.legend()
for j in range(k):
    plt.plot(new_gluc[j],new_hemo[j],marker='.',markersize=20)
    plt.plot(new_gluc[j],new_hemo[j],marker=str(centroid_number[j]),color='white')
plt.show()

#calculate accuaracy of the designated classifications
n=calculateDistanceArray(current_centroid[0],current_centroid[1],glucose,hemoglobin)
prediction=nearestCentroid(n)
true_pos=0
false_pos=0
true_neg=0
false_neg=0
for i in range(len(glucose)):
    if(prediction[i]==classification[i] and prediction[i]==0): true_pos+=1
    if(prediction[i]==classification[i] and prediction[i]==1): true_neg=1
    if(prediction[i]==1 and classification[i]==0): false_pos+=1
    if(prediction[i]==0 and classification[i]==1): false_neg+=1



