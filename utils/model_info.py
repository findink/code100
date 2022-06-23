def model_info(net):
    arg_total, arg_train, arg_not_train=0,0,0
    for p in net.parameters():
        n = p.nelement()
        arg_total += n
        if p.requires_grad:
            arg_train += n
        else:
            arg_not_train += n
    print("Model total arg:",arg_total)  
    print("Model total arg_trainable",arg_train)
    print("Model total arg_not_trainable",arg_not_train)
    print("Model total Mem use:",round(arg_total*4/1024/1024,2),"MB")
