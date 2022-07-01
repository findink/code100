import numpy as np


def ts_mask(x):
    x = x.copy()  # dont change origin
    block_len =  len(x)//3
    index = np.random.randint(0,len(x)-block_len,1)[0]
    x[index:index+block_len] = 0
    return x


    
def ts_permute(x,parts=5):
    x = x.copy()
    block_len = len(x)//parts
    index_list = [ i * block_len for i in range(parts+1)]
    y = x.copy()
    y[index_list[0]:index_list[1]] = x[index_list[parts-1]:index_list[parts]]
    for i in range(parts-1):
         y[index_list[i+1]:index_list[i+2]] = x[index_list[i]:index_list[i+1]]
    return y

def ts_repeat(x,n=3):
    x = x.copy()
    block_len =  len(x)//n
    index = np.random.randint(0,len(x)-block_len,3)
    x[index[-1]:index[-1]+block_len] = x[index[0]:index[0]+block_len]
#     x[index[n//2]:index[n//2]+block_len] = x[index[0]:index[0]+block_len]
    return x
    

def test_change(x,x1,t = 0.03):
    threshold = t * (max(x)-min(x))
    return np.sum(np.abs(x - x1))/len(x) >= threshold





def generate_anomaly(x_nor):
    "generate anomaly sample, num == len(x_nor)"
    y = []
    func_list = [ts_repeat,ts_mask,ts_permute]
    func_list_len = len(func_list)
    for i in range(len(x_nor)):
        xi = x_nor[i]
        func = func_list[i%func_list_len]
        yi = func(xi)
#         while not test_change(yi,xi):
#                 yi = func(xi)
        y.append(yi)  
         
    return np.array(y)
