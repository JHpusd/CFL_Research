import torch.nn as nn
import torch.nn.functional as F
import torch

'''
test = torch.Tensor([[5.0,4.0,2.0], [4.0, 2.0, 8.0], [4.0,4.0,1.0]])
labels = torch.tensor([0, 2, 1])

def get_nll(input, labels):
    probs = F.softmax(input, dim=1)

    # Gather the log-probabilities corresponding to the correct labels
    batch_size = len(input)
    nll_loss = -torch.log(probs[range(batch_size), labels])
    return nll_loss.mean()

print(get_nll(test, labels))

test = torch.Tensor([-2,-1,0,1,2])
test2 = [1,2,3,4,5]
print(type(test2))
test2 = torch.tensor(test2)
print(type(test2))
'''

test = [[-2,-1,0,1,2,3]]
print(-torch.log(test[0][3]))