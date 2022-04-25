import argparse

args = argparse.Namespace(
    lr= 1e-4,
    batch_size =8,
    train_size =0.8,
    weight_decay = 1.0,
    path ="./data/Images", #./data/Images,
    metadata = "./data/metadata_ok.csv" 

)
# we ask the user to input the number of epochs using pyhton3 main.py --modelresnet--num-epochs=10