import pandas as pd
import numpy as np
"""处理csv格式的数据文件，使之适配“prepare_data.py”文件中的传入csv文件格式"""
#原子质量对照表
atom2mass = {
    'H': 1.00783,
    'B': 11.00931,
    'C': 12.0,
    'N': 14.00307,
    'O': 15.99491,
    'F': 18.99840,
    'Si': 27.97693,
    'P': 30.97376,
    'S': 31.97207,
    'L': 34.96885,
    'R': 78.91834,
    'I': 126.90448,
    'E': 0.000548579908999924
}
#读取原始数据并显示
df_pfas_raw=pd.read_csv("./data/pfas/heigh_pfas_0125.csv")
print(df_pfas_raw)
print(df_pfas_raw.columns)
#读取原始数据中的分子质量，计算前体离子的质荷比(precursor_mz)
mol_mass=df_pfas_raw["mw"]
print(mol_mass)
precursor_mz=np.add(np.subtract(mol_mass,atom2mass["H"]),atom2mass["E"])
precursor_mz=precursor_mz.rename("precursor_mz")
print(precursor_mz)
#创建新Dataframe，改变结构与列名，将分子质量列(mw)替换为计算得到的前体离子质荷比列(precursor_mz)
df_pfas_processed=pd.DataFrame(columns=['smiles', 'tokens', 'formula', 'precursor_mz', 'mz', 'intensity'])
#print(df_pfas_processed)#调试用代码
df_pfas_processed["smiles"]=df_pfas_raw["smi"]
df_pfas_processed["tokens"]=df_pfas_raw["smi_token"]
df_pfas_processed["formula"]=df_pfas_raw["formula"]
df_pfas_processed["precursor_mz"]=precursor_mz
df_pfas_processed["mz"]=df_pfas_raw["mz"]
df_pfas_processed["intensity"]=df_pfas_raw["intensity"]
print(df_pfas_processed)
#存储处理后的数据
df_pfas_processed.to_csv(path_or_buf="./data/pfas/processed_heigh_pfas_0125.csv",index=False)