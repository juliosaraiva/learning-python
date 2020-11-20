import sys
import os
from PIL import Image

source_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.mkdir(output_folder)
    img_files = os.listdir(source_folder)
    for img in img_files:
        img_name = os.path.splitext(img)[0]
        png = Image.open(f'{source_folder}{img}')
        rgb = png.convert('RGB')
        rgb.save(f'{output_folder}{img_name}.jpg')

if __name__ == '__main__':
    pass
