import cv2
import os

img_path = "dataset_split/train"

files = os.listdir(img_path)

if files:
    file = files[0]
    full_path = os.path.join(img_path, file)

    img = cv2.imread(full_path)

    # Rotation
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Blur
    blurred = cv2.GaussianBlur(img, (5,5), 0)

    # Brightness
    bright = cv2.convertScaleAbs(img, alpha=1.2, beta=40)

    cv2.imwrite("outputs/rotated.jpg", rotated)
    cv2.imwrite("outputs/blurred.jpg", blurred)
    cv2.imwrite("outputs/bright.jpg", bright)

    print("Augmentation Complete")
    print("Saved in outputs/")
else:
    print("No images found")