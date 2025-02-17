from PIL import Image
import os

def resize_image(input_path, output_path, size=(360, 360)):
    with Image.open(input_path) as img:
        if img.size != size:
            img = img.resize(size, Image.LANCZOS)
        img.save(output_path)

def process_images(input_folder, output_folder, size=(360, 360)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, size)

if __name__ == "__main__":
    input_folder = r'C:\Users\vinay\OneDrive\Desktop\Github\Machine Learning Projects\Hand-Gesture-Recognition-for-Smart-TVs\Dataset\input_folder'
    output_folder = r'C:\Users\vinay\OneDrive\Desktop\Github\Machine Learning Projects\Hand-Gesture-Recognition-for-Smart-TVs\Dataset\output_folder'
    process_images(input_folder, output_folder)