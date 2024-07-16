import torch

print(torch.cuda.device_count())
print(torch.cuda.get_device_properties(0))
