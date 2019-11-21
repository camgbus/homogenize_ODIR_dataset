import os

# IMAGE RESOLUTION
dest_resolution = 512

# PATHS
# TODO: change
data_root = 'D:\\ODIR-5K_Training_Images' 
images_dir = os.path.join(data_root, 'ODIR-5K_Training_Dataset')
csv_labels = os.path.join(data_root, 'ODIR-5K_Training_Annotations(Updated)_V2.csv')
destination_root = 'C:\\Users\\cgonzale\\Documents\\data\\ODIR_'+str(dest_resolution)
data_destination = os.path.join(destination_root, 'train')
new_data_frames_destination = destination_root

