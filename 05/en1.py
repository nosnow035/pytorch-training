from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":
    image_path = r"C:\Users\north\pytorch講座\pytorch-training\05\dog_img.png"
    image = Image.open(image_path)

    preprocess_1 = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    processed_image = preprocess_1(image)
    plt.imshow(processed_image.permute(1, 2, 0))
    plt.show() 
