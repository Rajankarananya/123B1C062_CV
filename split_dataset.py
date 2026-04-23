import os
import random
import shutil

source = "dataset/State-wise_OLX"
target = "dataset_split"

train_path = os.path.join(target, "train")
val_path = os.path.join(target, "val")
test_path = os.path.join(target, "test")

for folder in [train_path, val_path, test_path]:
    os.makedirs(folder, exist_ok=True)

images = []

for root, dirs, files in os.walk(source):
    for file in files:
        if file.endswith((".jpg", ".jpeg", ".png")):
            images.append(os.path.join(root, file))

random.shuffle(images)

n = len(images)
train_end = int(0.7 * n)
val_end = int(0.85 * n)

train = images[:train_end]
val = images[train_end:val_end]
test = images[val_end:]

def copy_files(files, folder):
    for file in files:
        shutil.copy(file, folder)

copy_files(train, train_path)
copy_files(val, val_path)
copy_files(test, test_path)

print("Total Images:", n)
print("Train:", len(train))
print("Validation:", len(val))
print("Test:", len(test))
print("Dataset Split Complete")