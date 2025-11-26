from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

class ImageTransform():
 def __init__(self,resize,mean,std):
  self.data_transform = {
  'train' : transforms.Compose([
   

  ]),
  'val' : transforms.Compose([
   
    
 ])
 }
 def __call__(self, img,phase='tranin'):
  return self.data_transform[phase](img)

class MyDataset(Dataset):
    def __init__(self,img_list,transform=None,phase='train'):
     self.transform = transform
     self.phase = phase
     self.img_list = img_list
 
    def len(self):
     return len (self.img_list)

    def __getitem__(self,idx):
      img_path = self.img_list[idx]
