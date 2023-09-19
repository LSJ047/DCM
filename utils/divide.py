import pandas as pd
import os
from pathlib import Path


def divide_3(input_csv, output_path, d1, d2, d3):
    """将数据分为MSB、NSB和LSB三个部分"""
    # 从CSV文件中读取数据
    df = pd.read_csv(input_csv, header=None)

    n = d1 + d2 + d3
    # 对每个元素进行 x // 2^d 和 x % 2^d 操作
    result_channel1 = df.apply(lambda x: x // 2 ** (n-d1))
    df2 = df.apply(lambda x: x % 2 ** (n-d1))

    result_channel2 = df2.apply(lambda x: x // 2 ** d3)
    result_channel3 = df2.apply(lambda x: x % 2 ** d3)


    # 保存结果到CSV文件
    p = Path(input_csv)
    outputs = os.path.join(output_path, p.stem)
    if not os.path.exists(outputs):
        os.mkdir(outputs)
    s = str(d1) + str(d2) + str(d3)
    print(f"{p.stem}result_channel1 shape: {result_channel1.shape}")
    print(f"{p.stem}result_channel2 shape: {result_channel1.shape}")
    print(f"{p.stem}result_channel3 shape: {result_channel1.shape}")
    result_channel1.to_csv(os.path.join(outputs, s + 'MSB.csv'), index=False, header=False)
    result_channel2.to_csv(os.path.join(outputs, s + 'NSB.csv'), index=False, header=False)
    result_channel3.to_csv(os.path.join(outputs, s + 'LSB.csv'), index=False, header=False)


def divide_2(input_csv, output_path, d):
    """将数据分为MSB、NSB和LSB三个部分"""
    # 从CSV文件中读取数据
    df = pd.read_csv(input_csv, header=None)

    # 对每个元素进行 x // 2^d 和 x % 2^d 操作
    result_channel1 = df.apply(lambda x: x // 2 ** d)
    result_channel2 = df.apply(lambda x: x % 2 ** d)

    # 保存结果到CSV文件
    p = Path(input_csv)
    outputs = os.path.join(output_path, p.stem)
    if not os.path.exists(outputs):
        os.mkdir(outputs)
    print(f'{p.stem}result_channel1:{result_channel1.shape}')
    print(f'{p.stem}result_channel2:{result_channel2.shape}')
    result_channel1.to_csv(os.path.join(outputs, str(d) + '_MSB.csv'), index=False, header=False)
    result_channel2.to_csv(os.path.join(outputs, str(d) + '_LSB.csv'), index=False, header=False)
