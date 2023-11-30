
# import ultralytics
# import numpy as np
# import cv2
# import os
# from ultralytics import YOLO
# ultralytics.checks()

# MODEL = "best.pt"
# model = YOLO(MODEL)
# model.fuse()
# # dict maping class_id to class_name
# CLASS_NAMES_DICT = model.model.names
# # class_ids of interest - car, motorcycle, bus and truck
# print(CLASS_NAMES_DICT)
# pred = model(r"C:\Users\patil\Desktop\SIH Project\Ctrl-Alt-Defeat\sysllama.png",verbose = False)
# print(pred)
import ultralytics
from ultralytics import YOLO

MODEL = "best.pt"
model = YOLO(MODEL)
model.fuse()

CLASS_NAMES_DICT = model.model.names
print(CLASS_NAMES_DICT)

# Define the classes of interest (car, motorcycle, bus, truck)
classes_of_interest = ['car', 'motorcycle', 'bus', 'truck']

# Image path
image_path = r"sysllama.png"
output_path = r"C:\Users\patil\Desktop\SIH Project\Ctrl-Alt-Defeat\output_image.png"

# Make predictions on the image
predictions = model(image_path, show=True,verbose=False,save_txt = True)
print(predictions)
