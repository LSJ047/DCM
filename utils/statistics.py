import os
import pandas as pd
import numpy as np


def analyze_csv(file_path, out_path):
    # 读取CSV文件
    df = pd.read_csv(file_path, header=None)

    # 将数据转换成一维数组
    data = df.values.flatten()

    # 统计数字出现次数
    unique_values, counts = pd.Series(data).value_counts().sort_index().reset_index().values.T

    # 创建一个新的DataFrame，第一行为数字名称，第二行为出现次数
    result_df = pd.DataFrame([unique_values, counts])

    # 将结果保存到CSV文件
    result_df.to_csv(out_path, index=False, header=False)


def statistics(input_dir):
    output_dct_dir = os.path.join(os.path.dirname(input_dir), input_dir + '_statistics/')
    if not os.path.exists(output_dct_dir):
        os.mkdir(output_dct_dir)
    for file in os.listdir(input_dir):
        if file.endswith('.csv'):
            new_file_name = os.path.join(output_dct_dir, 'static_' + file)  # 新文件名
            analyze_csv(os.path.join(input_dir, file), new_file_name)


def analyze_dct_csv(file_path, out_path):
    # 读取CSV文件
    df = pd.read_csv(file_path, header=None)

    # 将数据转换成二维数组（8x8块）
    data = df.values.reshape(-1, 8, 8)

    # 去掉每块的第一个元素
    filtered_data = data[:, 1:, :][:, :, 1:].reshape(-1)


    # 统计数字出现次数
    unique_values, counts = np.unique(filtered_data, return_counts=True)

    # 创建一个新的DataFrame，第一行为数字名称，第二行为出现次数
    result_df = pd.DataFrame([unique_values, counts])

    # 将被删除的数字保存
    deleted_values = data[:, 0, 0].reshape(-1)
    deleted_df = pd.DataFrame([deleted_values])

    # 将结果保存到CSV文件
    result_df.to_csv(out_path, index=False, header=False)

    result_file_path = out_path.replace('.csv', '_remove.xlsx')
    # 将deleted_df保存到xlsx文件
    deleted_df.to_excel(result_file_path, index=False, header=False)


def statistics_dct(input_dir):
    output_dct_dir = os.path.join(os.path.dirname(input_dir), input_dir + '_statistics/')
    if not os.path.exists(output_dct_dir):
        os.mkdir(output_dct_dir)
    for file in os.listdir(input_dir):
        if file.endswith('.csv'):
            if 'LSB' in file:
                new_file_name = os.path.join(output_dct_dir, 'static_' + file)  # 新文件名
                analyze_dct_csv(os.path.join(input_dir, file), new_file_name)
            else:
                new_file_name = os.path.join(output_dct_dir, 'static_' + file)  # 新文件名
                analyze_csv(os.path.join(input_dir, file), new_file_name)