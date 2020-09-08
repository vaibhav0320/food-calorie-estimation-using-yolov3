import os
from random import shuffle
import argparse 

def arg_parse():
     
    parser = argparse.ArgumentParser(description='Train and test splittin tool')
   
    parser.add_argument("--path",type=str,required=True, help = 
                        "Path to dataset directory")
    parser.add_argument("--img",type=str,default="./data/images", help = 
                        "Name of directory containg images")
    parser.add_argument("--train_file",type=str,default="train.txt", help = 
                        "name of the output train file")
    parser.add_argument("--test_file",type=str,default="val.txt", help = 
                        "name of the output test file")
    parser.add_argument("--train_size",type=float,default=0.9, help = 
                        "Train size")  
    
    return parser.parse_args()

args = arg_parse()
train_size = args.train_size
test_size = 1-train_size
train_file = args.train_file
test_file = args.test_file

path = args.path
image_dir = args.img
os.chdir(path)
file_list = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
shuffle(file_list)

total_len = len(file_list)
train_len = int(total_len*train_size)
test_len = total_len-train_len

train_list = file_list[:train_len]
test_list = file_list[train_len:]

f = open(os.path.join(path,train_file),'w')
for image in train_list:
	f.write(os.path.join(path,image)+'\n')
f.close()

f = open(os.path.join(path,test_file),'w')
for image in test_list:
	f.write(os.path.join(path,image)+'\n')
f.close()





