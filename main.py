import argparse




print(__name__)

if __name__ == "__main__":
    print("hello")
    parser = argparse.ArgumentParser()
    parser.add_argument('--model',default="resnet50",choices=['resnet50','dilated_conv'],help = 'resnet is ok'   ) 
    parser.add_argument('--dataset',default="ECG200",help="200 is ok")
    parser.add_argument('--batch_size',type=int,default=125)
    parser.add_argument("--lr",type=float,default=0.01)
    parser.add_argument('--epoch',type=int,default=50)

    args = parser.parse_args()
    print(args)
    print(type(args.lr))

    
