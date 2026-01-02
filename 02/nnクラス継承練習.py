import torch
from torch import nn

class mymodel(nn.Module):
    def __init__(self,mytensor:torch.Tensor,elem_add:int,elem_multiply: int):
        super().__init__()#継承
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply

    def forward(self, x: torch.Tensor):    
     assert x.size() == self.mytensor.size(), "input size must match self.tensor size."
     problem2_out = x + self.mytensor
     problem3_out = problem2_out + self.elem_add
     problem4_out = problem3_out * self.elem_multiply # 数値を乗算
     return problem2_out, problem3_out, problem4_out

if __name__=="__main__":
    mymodel1 = mymodel(torch.ones((3, 3)), 4, 6)    
    p2out, p3out, p4out = mymodel1(torch.full((3, 3), 2))  #第1引数：テンソルの形（サイズ）第2引数：中を埋める値「3×3 の行列を、全部 2 で埋める」 という意味。一つのテンソルを作成
    """ 各テンソルを出力 """
    print("===== problem 2 =====")
    print(repr(p2out))
    print("===== problem 3 =====")
    print(repr(p3out))
    print("===== problem 4 =====")
    print(repr(p4out))