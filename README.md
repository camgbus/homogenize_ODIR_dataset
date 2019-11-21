# homogenize_ODIR_dataset

1. Install dependencies with 'pip install -r requirements.txt'
2. Save the excel table as a tab-separated csv file
3. Change the paths and desired output resolution in 'ho/paths.py'
4. Execute 'ho/homogenize_images.py' to remove edges of landscape images and unify resolution.
5. (optional) Execute 'ho/new_df.py' save the label information in two data frames, one for patient and one for image. The image DF includes information about image artifacts, such as 'blurred lens'.
