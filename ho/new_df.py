
# %%

from IPython import get_ipython
get_ipython().magic('load_ext autoreload') 
get_ipython().magic('autoreload 2')

import os
import csv
import sys
import pandas as pd
import numpy as np
from ho.paths import csv_labels, new_data_frames_destination

# Classes and picture characteristics from https://odir2019.grand-challenge.org/dataset/
picture_characteristics = ['lens dust', 'optic disk photographically invisible', 'low image quality', 'image offset']
labels = ['normal', 'diabetes', 'glaucoma', 'cataract', 'AMD', 'hypertension', 'myopia', 'others']

# Build 2 data frames: 1 per patient (with labels) and one per image (with characteristics)
labels_mapping = range(7, 15)
patient_df = []
image_df = []
with open(csv_labels) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    first = True
    for row in csv_reader:
        if first:
            first = False
            continue
        patient_id = row[3].split('_')[0]
        if patient_id:
            # Note that the ds is multi-label
            ground_truth = [int(row[i]) for i in labels_mapping]   
            male = 1 if 'Male' in row[2] else 0                 
            patient_df.append(tuple([patient_id, row[1], male] + ground_truth))
            image_df.append(tuple([patient_id, 1] + [1 if char in row[5] else 0 for char in picture_characteristics]))
            image_df.append(tuple([patient_id, 0] + [1 if char in row[6] else 0 for char in picture_characteristics]))

patient_df_cols = ['patient_id', 'age', 'male?'] + labels
image_df_cols = ['patient_id', 'left?'] + picture_characteristics
patient_df = pd.DataFrame(patient_df, columns=patient_df_cols)
image_df = pd.DataFrame(image_df, columns=image_df_cols)
assert len(patient_df) == 3500
assert len(image_df) == 7000

patient_df.to_csv(os.path.join(new_data_frames_destination, 'patient_df.csv'))
image_df.to_csv(os.path.join(new_data_frames_destination, 'image_df.csv'))


#%%
# Print out information about the data set
def print_class_distribution(df):
    class_dict = {label: len(df[df[label] == 1]) for label in labels}
    print(class_dict)

print('Class distribution regular train set')
print_class_distribution(patient_df)


print('Class distribution for the different image artifacts')
for char in picture_characteristics:
    char_df = image_df[image_df[char] == 1]
    char_patient_df = patient_df[patient_df['patient_id'].isin(char_df['patient_id'])]
    print_class_distribution(char_patient_df)


print('Class distribution for the subset of images with ANY artifact')
char_df = image_df[(image_df['lens dust'] == 1) | (image_df['optic disk photographically invisible'] == 1) | 
    (image_df['low image quality'] == 1) | (image_df['image offset'] == 1)]
char_patient_df = patient_df[patient_df['patient_id'].isin(char_df['patient_id'])]
print_class_distribution(char_patient_df)

# %%
from ho.display_images import random_img_grid
from ho.paths import data_destination

# Print out grid of images of a class
def print_grid(patient_df, image_df, label=None, characteristic=None):
    if label:
        patient_df = patient_df[patient_df[label] == 1]
    patients = list(patient_df['patient_id'])
    if characteristic:
        char_df = image_df[(image_df[characteristic] == 1)]
        images = [row['patient_id'] + ('_left.png' if row['left?'] else '_right.png') for index, row in char_df.iterrows()]
        patient_paths = [os.path.join(data_destination, x) for x in images]
    else:
        patient_paths = [os.path.join(data_destination, x +'_left.png') for x in patients]
    random_img_grid(img_path_list=patient_paths, nr_rows=2, nr_cols=4, save_path='C:\\Users\\cgonzale\\Desktop\\Thesis images\\ODIR\\'+str(label)+'_'+str(characteristic)+'.png')
