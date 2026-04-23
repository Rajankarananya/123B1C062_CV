import os

path = "dataset/State-wise_OLX"

for folder in os.listdir(path):
    files = os.listdir(path + "/" + folder)
    jpgs = [f for f in files if f.endswith(".jpg")]
    print(folder, len(jpgs))