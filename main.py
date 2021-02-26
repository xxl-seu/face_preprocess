from face_preprocess import *

img = cv2.imread('006_05562.jpg').astype(np.uint8) # [H, W, C]

# 创建人脸preprocess的3个类方法
face_dector = preprocess_landmarks()
face_rotate = preprocess_rotate()
face_crop = preprocess_crop()

coordinates = face_dector.detect(img) # 返回人脸关键点landmarks
angle = face_rotate.eye_angle(coordinates) # 返回人眼测得所需摆正角度
rot_img, rot_coordinates = face_rotate.rotate(img, angle, coordinates) # 摆正图片及landmarks
crop_img = face_crop.crop( rot_coordinates, img, 0.2) # 裁剪人脸图片

cv2.imwrite('crop_img.jpg',crop_img) # 存储图像