from PIL import Image
import os

# input_file_1 = test_input.jpg
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "test_input.jpg")

# input_file_2 = input.dng

with open(f"{image_path}" , "rb") as f :
    img1 = f.read()
    
# with open(f"input_file_2" , "rb") as f :
#     img2 = f.read()

print(img1)
# print(img2)
