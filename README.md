
#  Real-time-object-detection-and-buzzer

# Computer vision
Computer vision is a field of artificial intelligence that trains computers to interpret and understand the visual world. 
Using digital images from cameras and videos and deep learning models, machines can accurately identify and classify objects.

Many popular computer vision applications.
    Object Classification
    Object Identification 
    Object Verification
    Object Detection 
    Object Landmark Detection
    Object Segmentation
    Object Recognition
  
In this project I used open cv library to detect objects(any) in the image and make buzzer if any object is present or moving

# Applications of the project
1.Survilence camera  to detect any unknown object passing over and to activate alert system if any object gets detected.
2.Continuous monitoring of the goods/products
3.Theft detection
4.Continuous monitoring of baby

# Procedure

# Import libraries
Open cv library to work with image/video and winsound to make buzzer

![image](https://user-images.githubusercontent.com/69953585/110923627-1b5e1780-8347-11eb-83a8-39db6fe71165.png)


# Intialize camera
Intialize camera and load frames of image 
First assign base or initial image by taking first image frame.
After getting images, convert it to gray scale image 
Apply gaussian blurr filter to remove unwanted noise in the image
Then convert it to binary image
Apply morphological operations like dialtion and erosion to remove unwanted small dot pixels in the image
Then evaluate the current binary image with the initial /base image.
If any difference which exceeds the predefined threshold the activate alert system.








