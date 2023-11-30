import os
from ultralytics import YOLO
import shutil

MODEL = "best.pt"
model = YOLO(MODEL)
model.fuse()

CLASS_NAMES_DICT = model.model.names
print(CLASS_NAMES_DICT)

# Define the classes of interest (car, motorcycle, bus, truck)
classes_of_interest = ['car', 'motorcycle', 'bus', 'truck']

# Image path
image_path = r"lol.jpeg"
output_path = r"C:\Users\patil\Desktop\SIH Project\Ctrl-Alt-Defeat\output_image.png"

# Make predictions on the image
predictions = model(image_path, verbose=False, save_txt=True)
print(predictions)

# Check if the txt file is generated in the given directory
txt_file_path = r"runs\detect\predict\labels\lol.txt"  # Update this path as needed
file_exists = os.path.exists(txt_file_path)

if file_exists:
    print("Text file generated.")
    # Delete the text file
    os.remove(txt_file_path)
    print("Text file deleted.")
    result = True
else:
    print("Text file not generated.")
    result = False

print("Result:", result)
folder_path = r"C:\Users\patil\Desktop\SIH Project\Ctrl-Alt-Defeat\runs\detect"
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)

    # Check if the item is a directory
    if os.path.isdir(item_path):
        try:
            # Remove the directory and its contents
            shutil.rmtree(item_path)
            print(f"Removed folder: {item_path}")
        except Exception as e:
            print(f"Failed to remove folder: {item_path} - {e}")