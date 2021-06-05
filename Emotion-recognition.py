from fer import FER  #Facial Expression Recognition with a deep neural network using Tensorflow and Keras libraries

import matplotlib.pyplot as plt 

img = plt.imread("img.jpg")  #reading the image into an array
detector = FER(mtcnn=True)  #mtcnn is multicascade covolution network
emotion, score = detector.top_emotion(img)   #detecting the dominant emotion and its score
print(emotion,score)  
