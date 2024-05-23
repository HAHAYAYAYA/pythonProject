import torch
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter('logs')
image_path = 'dataset/train/bees_images/29494643_e3410f0d37.jpg'
img_PIL = Image.open(image_path) #PIL型对象
img_array = np.array(img_PIL)    #numpy型对象
print(type(img_array))
print(img_array.shape)

writer.add_image("bees3", img_array, 3, dataformats='HWC')


#y = x
for i in range(100):
    writer.add_scalar("y=2x", 2*i, i)

#test
writer.close()