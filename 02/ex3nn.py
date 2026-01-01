import torch
from torch import nn

class mymodel(nn.Modules):
    def __init__(self,mytensor:torch.Tensor,elem_add:int,elem_multiply: int):
        super().__init__()#継承
        self.mytensor = mytensor
        self.elem_add = elem_multiply

""""forward"""

def forward(self, x: torch.Tensor):
    
    assert x.size() == self.mytensor.size(), "input size must match self.tensor size."
    problem2_out = x + self.myrensor
    problem3_out = problem2_out + self.elem_add
    problem4_out = problem3_out * self.elem_multiply # 数値を乗算
    return problem2_out, problem3_out, problem4_out