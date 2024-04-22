import os
import random
import shutil

def select_random_images(source_dir, destination_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get list of all image files in source directory
    image_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    # Calculate 20% of the total number of images
    n = int(len(image_files) * 0.2)

    # Check if the number of images in the source directory is less than n
    if len(image_files) < n:
        print("Error: Number of images in source directory is less than", n)
        return

    # Select n random images
    random_images = random.sample(image_files, n)

    # Copy selected images to destination directory
    for img in random_images:
        shutil.move(os.path.join(source_dir, img), destination_dir)


select_random_images("ED_Dataset/Angry", "ED_Dataset/test_set/Angry")
select_random_images("ED_Dataset/Happy", "ED_Dataset/test_set/Happy")
select_random_images("ED_Dataset/Neutral", "ED_Dataset/test_set/Neutral")
select_random_images("ED_Dataset/Sad", "ED_Dataset/test_set/Sad")
select_random_images("ED_Dataset/Surprise", "ED_Dataset/test_set/Surprise")
