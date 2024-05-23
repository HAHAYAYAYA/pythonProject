import torch
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('logs')

# writer.add_image('image', torch.rand(3, 3, 3, 3))
writer.add_scalar('scalar', torch.rand(3, 3, 3, 3))
writer.close()