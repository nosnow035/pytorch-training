import torch
from torch import nn

class ExcerciseModel(nn.Module): #画像から数値64個（特徴）を出力 128×128の画像
    def __init__(self, out_features=64):
        super().__init__()
        self.conv = nn.Conv2d(in_channels=3,out_channels=256,kernel_size=5,stride=8)
        self.bn = nn.BatchNorm2d(num_features=256) #outchanersのところ
        self.relu = nn.ReLU()
        in_features = 256 * 16 * 16 #1画像の256枚特徴マップの16×16の画像全数値
        self.fc = nn.Linear(in_features=in_features, out_features=out_features,bias=True) #最後に64個の特徴を作成 全結合層

    def forward(self,x): #層を重ねる
         x = self.conv(x)
         x = self.bn(x)
         x = self.relu(x)
         x = torch.flatten(x, 1)
         x = self.fc(x)
         return x
    


    