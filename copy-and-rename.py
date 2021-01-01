from shutil import copyfile
from PIL import Image, ImageEnhance
import PIL
import os

parent_dir = os.getcwd()

files = [f for f in os.listdir('.') if os.path.isfile(f)]

os.mkdir(os.path.join(parent_dir, 'diamond'))
os.mkdir(os.path.join(parent_dir, 'netherite'))

for f in files:
    copyfile(f, os.path.join('diamond', f))
    copyfile(f, os.path.join('netherite', f))

    if 'properties' in f:
        os.system(f"sed -i 's/diamond/netherite/g' {os.path.join('netherite', f)}")

    if 'png' in f:
        netherite_image_path = os.path.join(parent_dir, 'netherite', f)
        img = Image.open(netherite_image_path)
        img = ImageEnhance.Color(img).enhance(0.5)
        img = ImageEnhance.Brightness(img).enhance(0.3)
        img.save(netherite_image_path)

    os.system(f"trash {f}")
