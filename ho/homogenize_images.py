#%%
import os
from PIL import Image
from ho.paths import images_dir, data_destination, dest_resolution

# Create destination directory
if not os.path.exists(data_destination):
    os.makedirs(data_destination)

for file_name in os.listdir(images_dir):
    img_path = os.path.join(images_dir, file_name)
    pill_img = Image.open(img_path)
    # Center-crop
    width, height = pill_img.size
    if width != height:
        if height > width:
            top = int((height - width)/2)
            bottom = top + width
            cropping_area = (0, top, width, bottom)
        else:
            left = int((width - height)/2)
            right = left + height
            cropping_area = (left, 0, right, height)
        pill_img = pill_img.crop(cropping_area)
    # Change resolution
    pill_img = pill_img.resize((dest_resolution, dest_resolution))
    pill_img.save(os.path.join(data_destination, file_name.split('.jpg')[0]+'.png'))

# %%