import torch
from torch import nn

if __name__ == "__main__":
    #Tenorを定義
    #実際に学習に使われるデータは，
    #　(Batchsize, channel, width, height)
    #という形状
    my_tensor = torch.ones((32,1024))
    print(f"original : {my_tensor.shape}")

    fc = nn.Linear(in_features=1024,out_features=256,bias = True)
    out = fc(my_tensor)
    print(f"out1:{out.shape}")

    fc2 = nn.Linear(in_features=1024,out_features=2048,bias = True)
    out2 = fc2(my_tensor)
    print(f"out2:{out2.shape}")
    



