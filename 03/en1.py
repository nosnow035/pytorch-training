import torch
from torch import nn

if __name__ == "__main__":
    #Tenorを定義
    #実際に学習に使われるデータは，
    #　(Batchsize, channel, width, height)
    #という形状Conv2dは
    my_tensor = torch.ones((32, 3, 128, 128))
    print(f"original : {my_tensor.shape}")

    #畳み込み定義＆適用
    print("===problem2===")
    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3) #問２ stride=1 padding=0が初期値
    out = conv(my_tensor)
    print(f"out1 : {out.shape}")
    
    print("===problem3===")
    conv2 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3,stride=2,padding = 1)
    out2 = conv2(my_tensor)
    print(f"out2 : {out2.shape}")

    print("===problem4===")
    conv3 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5,stride=1,padding = 1)  #目標32×64×126×126
    conv4 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5,stride=2,padding = 2)  #目標32×256×64×64
    out3 = conv3(my_tensor)
    out4 = conv4(my_tensor)

    print(f"out3 : {out3.shape}")
    print(f"out4 : {out4.shape}")


