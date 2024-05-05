import csv
import os
import cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image

# Train Image Function
def TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message, text_to_speech):

    recognizer = cv2.face.LBPHFaceRecognizer_create() #LBPH face recognizer and a face detector using Haarcascades
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Id = getImagesAndLables(trainimage_path)
    recognizer.train(faces, np.array(Id))#image train hogi yaha pr
    recognizer.save(trainimagelabel_path)#to save trained recognizer in file
    res = "Image Trained successfully  Registration Done"
    message.configure(text=res)
    text_to_speech(res)

#  for getting images and corresponding labels for training
def getImagesAndLables(path):
    
    newdir = [os.path.join(path, d) for d in os.listdir(path)] # Get the paths of all images 
    imagePath = [
        os.path.join(newdir[i], f)
        for i in range(len(newdir))
        for f in os.listdir(newdir[i])
    ]
    
    #  empty lists to store images and labels
    faces = []
    Ids = []

    # Loop through each image path
    for imagePath in imagePath:
        # Open the image, convert it to grayscale, and convert to NumPy array
        pilImage = Image.open(imagePath).convert("L")# Open the image, convert to grayscale and NumPy array
        imageNp = np.array(pilImage, "uint8")
        Id = int(os.path.split(imagePath)[-1].split("_")[1])# Extract the label (Id) 
        
        # image array and image label
        faces.append(imageNp)
        Ids.append(Id)
    
    # lists of images and labels
    return faces, Ids


