#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:20:56 2020

@author: emeliadaro
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:58:51 2020

@author: emeliadaro
"""

#EMMY DARO
#K-MEANS CLUSTERING FUNCTIONS
#PROJECT 2 PART 5
#TIME SPENT: 8 hours

import numpy as np
import random 

#openckdfile()
#Reads in the ckd data set
#Takes no inputs
#Returns glucose, hemoglobin, and classification arrays

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#normalizeData()
#scales glucose and hemoglobin data into values between 0 and one so one is not weighed more than the other
#Takes glucose, hemoglobin, and classification arrays
#Returns scaled versions of glucose, hemoglobin, and classification arrays


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

#randomCentoid()
#Makes a random  value between 0 and 1
#Takes no inputs
#Returns a random value

def randomCentroid():
    return random.random()

#calculateDistanceArray()
#Finds the distance between every point and the centoids and stores it in an array
#Takes the scaled glucose and hemoglobin arrays and the random glucose and hemoglobin test case
#Returns an array of all the distances between the centoids and each other point in the data set


def calculateDistanceArray(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled):
    distance_array=[]
    np.array(distance_array)
    for n in range(k):
        for i in range(len(glucose)):
            distance=np.sqrt(((glucose_scaled[i]-new_gluc)**2)+((hemoglobin_scaled[i]-new_hemo)**2))
            distance_array=np.append(distance_array,[distance])
    return distance_array

#nearestCentroid()
#Assigns each point in the set to one of k centroids
#Takes distance array as the input
#Returns an array of cluster assignments/clssifications
#

def nearestCentroid(val):
    cluster_assign=np.zeros((len(glucose)))
    for i in range(len(glucose)):
        n=np.argmin(val[i])
        cluster_assign[i]=n
    return cluster_assign

#newCentroid()
#Calculates the new locations of the k centroids based on the averages for each point in that cluster
#Takes centroid position array as an input
#Returns new cluster positions
#

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
    
#updateCentoid()
#Calls previous functions in sequence to continually update the centroid position
#Takes the scaled glucose and hemoglobin arrays and the centroid position
#Returns the final centroid position


def updateCentroid(new_hemo,new_gluc,glucose,hemoglobin):
    x=calculateDistanceArray(new_hemo,new_gluc,glucose,hemoglobin)
    c=nearestCentroid(x)
    new_centroid=newCentroid(c)
    return new_centroid
    
    
    

