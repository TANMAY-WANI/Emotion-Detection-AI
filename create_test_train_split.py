import os
import random
import shutil

def select_random_images(source_dir, destination_dir, n):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get list of all image files in source directory
    image_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    # Check if the number of images in the source directory is less than n
    if len(image_files) < n:
        print("Error: Number of images in source directory is less than", n)
        return

    # Select n random images
    random_images = random.sample(image_files, n)

    # Copy selected images to destination directory
    for img in random_images:
        shutil.move(os.path.join(source_dir, img), destination_dir)
        print(f"Selected image: {img}")


select_random_images("Dataset/anger","Dataset/test_set/anger" ,27)
select_random_images("Dataset/contempt","Dataset/test_set/contempt" ,11)
select_random_images("Dataset/disgust","Dataset/test_set/disgust" ,35)
select_random_images("Dataset/fear","Dataset/test_set/fear" ,15)
select_random_images("Dataset/happy","Dataset/test_set/happy" ,41)
select_random_images("Dataset/sadness","Dataset/test_set/sadness" ,17)
select_random_images("Dataset/surprise","Dataset/test_set/surprise" ,50)
