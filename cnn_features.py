import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

model = models.resnet18(weights=None)
model.eval()

img = Image.open("outputs/cropped_plate.jpg").convert("RGB")

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

x = transform(img).unsqueeze(0)

with torch.no_grad():
    output = model(x)

print("CNN Feature Extraction Complete")
print("Output Shape:", output.shape)