# Face-preprocess

## Purpose

This file is used to handle the face preprocess problems, especially when you are dealing with the pictures in emotion database.

Including return 68 face landmarks, set the face right according to the angle which is calculated by landmarks on eyes, rotate the image and the landmarks by angle, crop the face by the margin as you like.

## Usage

You will see three files in master. Including a image named '006_05562.jpg', two python files 'face_preprocess.py', 'main.py'.

Put them in the same folder. 

Run 'main.py' directly, and you will get the croped image 'crop_img.jpg' saved in the same folder.

## Tips

This file can only be used to handle the image with one face inside, otherwise adjust the codes in 'face_preprocess.py' of line 21. Use 'For loop' traverse all the faces in image.

The file used to detect landmarks 'shape_predictor_68_face_landmarks.dat' should be downloaded by yourself, the URL is in the following:

[Download face landmarks detector 'shape_predictor_68_face_landmarks.dat'](https://pypi.org/simple/dlib/)

Dlib library is necessary, install it with commands'pip install dlib', remember to install cmake and boost before install dlib which is relied on them, of course with 'Visual studio 20XX' to provide C++ environment.(TOO TROUBLESOME!!!)
