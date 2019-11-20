import os

data_root = 'D:\\ODIR-5K_Training_Images'

images_dir = os.path.join(data_root, 'ODIR-5K_Training_Dataset')
# I saved the excel table as a tab-separated csv file (Field delimiter: Tab, String delimiter: "")
csv_labels = os.path.join(data_root, 'ODIR-5K_Training_Annotations(Updated)_V2.csv')



data_destination = 'D:\\ODIR-5K_Training_Images\\new'
#pip install -r requirements.txt