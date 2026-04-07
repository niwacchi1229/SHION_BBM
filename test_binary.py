from PIL import Image
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path_1 = os.path.join(script_dir, "test_input.jpg")
image_path_2 = os.path.join(script_dir, "input.dng")

with open(f"{image_path_1}" , "rb") as f :
    img1 = f.read()
    
with open(f"{image_path_2}" , "rb") as f :
    img2 = f.read()

print(img1)
print(img2)
