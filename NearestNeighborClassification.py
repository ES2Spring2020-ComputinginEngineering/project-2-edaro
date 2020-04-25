#EMMY DARO
#ES-02 PROJECT 2 PARTS 2 AND 3
#time spent: about 4 hours


import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats 


# FUNCTIONS

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
    hemoglobin_scaled = []
    np.array(hemoglobin_scaled)
    for i in range(len(glucose)):
        gluc_val=(glucose[i]-70)/(490-70)
        hemo_val=(hemoglobin[i]-3.1)/(17.8-3.1)
        glucose_scaled=np.append(glucose_scaled,[gluc_val])
        hemoglobin_scaled=np.append(hemoglobin_scaled,[hemo_val])
    return glucose_scaled, hemoglobin_scaled, classification

#createTestCase()
#Makes a random glucose and hemoglobin value between 0 and 1
#Takes no inputs
#Returns a random glucose value and a random hemoglobin value


def createTestCase():
    new_hemo=random.random()
    new_gluc=random.random()
    return new_hemo, new_gluc 

#calculateDistanceArray()
#Finds the distance between every point and the random test case and stores it in an array
#Takes the scaled glucose and hemoglobin arrays and the random glucose and hemoglobin test case
#Returns an array of all the distances between the point and each other point in the data se


def calculateDistanceArray(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled):
    distance_array=[]
    np.array(distance_array)
    for i in range(len(glucose)):
        distance=np.sqrt(((glucose_scaled[i]-new_gluc)**2)+((hemoglobin_scaled[i]-new_hemo)**2))
        distance_array=np.append(distance_array,[distance])
    return distance_array

#nearestNeighborClassifier()
#Finds the minimum distance in the distance array and assigns the test case the same classification as that point
#Takes the random test case, scaled glucose and hemoglobin arrays, and the classification array
#Returns a classification of the test case


def nearestNeighborClassifier(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled,classification):
    distance_array=calculateDistanceArray(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled)
    sort_index=np.argsort(distance_array)
    closest_index=sort_index[0]
    classifier=classification[closest_index]
    return classifier

#kNearestNeighborClassifier()
#Picks a designated number of closest points to the test case and assigns the classification of the majority of these points
#Takes the random test case, scaled glucose and hemoglobin arrays, and the classification array
#Returns a classification of the test case


def kNearestNeighborClassifier(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled,classification):
    distance_array=calculateDistanceArray(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled)
    sort_index=np.argsort(distance_array)
    k_indices = sort_index[:6]
    k_classifications = classification[k_indices]
    k_classifier = stats.mode(k_classifications)
    return k_classifier

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose,hemoglobin,classification)
new_hemo, new_gluc = createTestCase()
classifier=nearestNeighborClassifier(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled,classification)
print('nearest neighbor classification result:')
print(classifier)
k_classifier=kNearestNeighborClassifier(new_hemo,new_gluc,glucose_scaled,hemoglobin_scaled,classification)
print('K-nearest neighbot classification result:')
print(k_classifier[0])

plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()

plt.figure()
plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
plt.plot(new_hemo,new_gluc, "g.", markersize=10,label = "Test Case")
plt.xlabel("Hemoglobin Scaled")
plt.ylabel("Glucose Scaled")
plt.legend()
plt.show()
