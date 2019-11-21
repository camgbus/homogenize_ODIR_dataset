from PIL import Image
import matplotlib.pyplot as plt

def create_img_grid(img_path_grid = [['img.png']], img_size = (512, 512), 
    margin = (15, 15), background_color = (255, 255, 255, 255), save_path=None):
    bg_width = len(img_path_grid[0])*img_size[0] + (len(img_path_grid[0])+1)*margin[0]
    bg_height = len(img_path_grid)*img_size[1] + (len(img_path_grid)+1)*margin[1]
    new_img = Image.new('RGBA', (bg_width, bg_height), background_color)
    left = margin[0]
    top = margin[1]
    for row in img_path_grid:
        for img_path in row:
            img = Image.open(img_path)
            img = img.resize((img_size[0], img_size[1]))
            new_img.paste(img, (left, top))
            left += img_size[0] + margin[0]
        top += img_size[1] + margin[1]
        left = margin[0]
    if save_path is None:
        new_img.show()
    else:
        new_img.save(save_path)

import random
def random_img_grid(img_path_list, nr_rows, nr_cols, save_path=None):
    random.shuffle(img_path_list)
    img_path_grid = [[img_path_list[i+j*nr_cols] for i in range(nr_cols)] for j in range(nr_rows)]
    create_img_grid(img_path_grid=img_path_grid, save_path=save_path)