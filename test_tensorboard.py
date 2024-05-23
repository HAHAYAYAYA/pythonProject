import torch
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('logs')

# writer.add_image('image', torch.rand(3, 3, 3, 3))
#y = x
for i in range(100):
    writer.add_scalar("y=2x", 2*i, i)

#test
writer.close()