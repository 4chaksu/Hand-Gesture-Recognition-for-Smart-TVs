import os
from PIL import Image

# input_folder = r'C:\Dataset\Project_data\train'
# output_folder = r'C:\Dataset\Project_data\train_resized'
input_folder = r'C:\Dataset\Project_data\val'
output_folder = r'C:\Dataset\Project_data\val_resized'
new_size = (160, 120)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(('jpg', 'jpeg', 'png')):
            file_path = os.path.join(root, file)
            img = Image.open(file_path)
            img_resized = img.resize(new_size, Image.LANCZOS)
            
            # Create the corresponding directory in the output folder
            relative_path = os.path.relpath(root, input_folder)
            output_dir = os.path.join(output_folder, relative_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            output_path = os.path.join(output_dir, file)
            img_resized.save(output_path)
            print(f'Resized and saved {file_path} to {output_path}')
