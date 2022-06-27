# From: @lgq of CN/HITSZ/IOTS, 2022/06;
# To  : Everyone; with MIT license;
# What: timeseries to vec ; 
#       input : ts
#       output: vec
# Updater:

import torch
from torch import nn
import torch.nn.functional as F
import numpy as np


class SameShapeConv(nn.Module):
    '''
        conv but  shape dont change 
    '''
    def __init__(self,in_channels,out_channels,kernel_size,dilation=1):
        super().__init__()
        self.receptive_field = (kernel_size -1) * dilation + 1
        padding = self.receptive_field //2
        self.conv = nn.Conv1d(in_channels,out_channels,kernel_size,padding=padding,dilation=dilation)
        
    def forward(self,x):
        out = self.conv(x)
        return out if self.receptive_field % 2 != 0 else out[:,:-1]
        

class ConvBlock(nn.Module):
        '''conv block:
            two sameshapeconv
            with residual
        '''
        def __init__(self,in_channels,out_channels,kernel_size,dilation=1):
            super().__init__()
            self.conv1 = SameShapeConv(in_channels,out_channels,kernel_size,dilation=dilation)
            self.conv2 = SameShapeConv(out_channels,out_channels,kernel_size,dilation=dilation)
            self.projector = nn.Conv1d(in_channels,out_channels,1)  if in_channels != out_channels else None

        def forward(self,x):
            residual = x if self.projector is None else self.projector(x)
            out = F.gelu(x)
            out = self.conv1(out)
            out = F.gelu(out)
            out = self.conv2(out)
            return out + residual
        

class DilatedConvEncoder(nn.Module):
    '''
            
    '''
    def __init__(self,in_channels,channels,kernel_size): # channels: hiddle layer and output  channels list
        super().__init__()
        self.net = nn.Sequential(
                *[ ConvBlock(in_channels if i==0 else channels[i-1], channels[i], kernel_size, dilation=2**i) 
                       for i in range(len(channels))]
        )
        
    def forward(self,x):
        return self.net(x)
