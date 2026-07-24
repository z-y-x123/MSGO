import argparse
import pandas as pd
import json
def train_test_dev_split(args):
    """将数据集随机划分为test/dev/train三部分"""
    idx=args.idx#用于区分不同随机种子生成test/val/train数据集
    path=args.pfas_csv_path#文件路径
    df_pfas_temp=pd.read_csv(path)#读取文件
    #frac_input=args.frac#分割比例
    num_val=args.num_val#val数据集数据条数
    num_test=args.num_test#test数据集数据条数
    random_state_input=args.random_state#随机种子
    #将数据分为train\test\val三部分
    df_pfas_val=df_pfas_temp.sample(n=num_val,random_state=random_state_input)
    df_pfas_temp=df_pfas_temp.drop(df_pfas_val.index)
    df_pfas_test=df_pfas_temp.sample(n=num_test,random_state=random_state_input)
    df_pfas_train=df_pfas_temp.drop(df_pfas_test.index)
    #创建split_json文件
    infos={"train":list(df_pfas_train.index),"val":list(df_pfas_val.index),"test":list(df_pfas_test.index)}
    print(infos)
    with open(args.json_path,"w") as f:#将其以json文件格式存储到指定位置
        json.dump(infos,f)
    #分别存储train/test/val数据集
    df_pfas_train.to_csv(f"./data/pfas/heigh_pfas_0125_train_{idx}.csv",index=False)
    df_pfas_test.to_csv(f"./data/pfas/heigh_pfas_0125_test_{idx}.csv",index=False)
    df_pfas_val.to_csv(f"./data/pfas/heigh_pfas_0125_val_{idx}.csv",index=False)
    return

if __name__=="__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("--pfas_csv_path",default="./data/pfas/processed_heigh_pfas_0125.csv")
    parser.add_argument("--json_path",default="./data/pfas/pfas_split_info.json")
    parser.add_argument("--num_val",type=int,default=1000)
    parser.add_argument("--num_test",type=int,default=1000)
    parser.add_argument("--random_state",type=int,default=314)
    parser.add_argument("--idx",type=int,default=1)

    #读取参数
    args_input=parser.parse_args()
    #调用函数
    train_test_dev_split(args_input)