from torch.utils.data import Dataset
#import cv2 # pip install opencv-python
from PIL import Image
import os

class MyDataset(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir                #"dataset/train"
        self.label_dir = label_dir              #"ants"
        self.path = os.path.join(self.root_dir, self.label_dir)     #"dataset/train\\ants"
        self.image_path = os.listdir(self.path) #path文件下的文件做列表


    def __len__(self):
        return len(self.image_path)         #返回列表长度


    def __getitem__(self, index):
        image_name = self.image_path[index]
        image_item_path = os.path.join(self.path, image_name)
        image = Image.open(image_item_path)
        label = self.label_dir
        return image, label

root_dir = "./dataset/train"
ants_label_dir = "ants_images"
bees_label_dir = "bees_images"
ants_dataset = MyDataset(root_dir, ants_label_dir)
bees_dataset = MyDataset(root_dir, bees_label_dir)

train_dataset = ants_dataset + bees_dataset
