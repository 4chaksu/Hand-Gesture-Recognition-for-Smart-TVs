import os
from PIL import Image

def get_image_resolutions(input_folder):
    resolutions = {}
    
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                try:
                    with Image.open(os.path.join(root, file)) as img:
                        resolution = img.size
                        if resolution in resolutions:
                            resolutions[resolution] += 1
                        else:
                            resolutions[resolution] = 1
                except Exception as e:
                    print(f"Error processing file {file}: {e}")
    
    return resolutions

def print_resolutions(resolutions):
    for resolution, count in resolutions.items():
        print(f"Resolution {resolution}: {count} images")

if __name__ == "__main__":
    input_folder = r"C:\Dataset\Project_data\val_resized"  # Replace with your input folder path
    resolutions = get_image_resolutions(input_folder)
    print_resolutions(resolutions)  