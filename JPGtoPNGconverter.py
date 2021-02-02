###### how to use
###### python JPGtoPNGconverter.py thefoldercontainsjpgimgs thenewfolder

import sys
import os
from PIL import Image

# Grap first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check is new/ exists, if not create it
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

# loop through poks.
for imgname in os.listdir(image_folder):
  img = Image.open(f'{image_folder}{imgname}')
  clear_name = os.path.splitext(imgname)[0]
  img.save(f'{output_folder}{clear_name}.png', 'png')

print('all done!')
# convert images to png.
# save to the new folder.