import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

# torch.manual_seed(1)    # reproducible

x = torch.linspace(-1, 1, 100) .reshape(100,1)# x data (tensor), shape=(100, 1)
y = 0.2*torch.rand(x.size())
print(y)
# y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)
# plt.plot(x,y)
# plt.show()
x = F.relu(x)
print(x)