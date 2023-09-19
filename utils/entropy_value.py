import pandas as pd
import numpy as np
from scipy.stats import entropy


def calculate_entropy(file_path):
    # 从CSV文件读取数据
    df = pd.read_csv(file_path, header=None)
    pixel_values = df.iloc[0].values
    pixel_counts = df.iloc[1].values

    # 计算像素值的概率分布
    total_pixels = pixel_counts.sum()
    pixel_probabilities = pixel_counts / total_pixels

    # 计算信息熵
    entropy_value = entropy(pixel_probabilities, base=2)
    # entropy_value = -np.sum(pixe l_probabilities * np.log2(pixel_probabilities + np.finfo(float).eps))

    # 保存结果到同名txt文件中
    result_file_path = file_path.replace('.csv', '.txt')
    with open(result_file_path, 'w') as file:
        file.write(f'{entropy_value}')
    return entropy_value


def calculate_entropy_not0(file_path):
    # 从CSV文件读取数据
    df = pd.read_csv(file_path, header=None)
    pixel_values = df.iloc[0].values
    pixel_counts = df.iloc[1].values

    non_zero_pixels = pixel_values[pixel_values != 0]
    non_zero_counts = pixel_counts[pixel_values != 0]
    # print(pixel_counts)
    # 计算像素值的概率分布
    total_pixels = non_zero_counts.sum()
    pixel_probabilities = non_zero_counts / total_pixels

    # 计算信息熵
    entropy_value = entropy(pixel_probabilities, base=2)

    # 保存结果到同名txt文件中
    result_file_path = file_path.replace('.csv', 'not0.txt')
    with open(result_file_path, 'w') as file:
        file.write(f'{entropy_value}')

    return entropy_value


def calculate_dct_entropy(file_path):
    # 从CSV文件读取数据
    df = pd.read_csv(file_path, header=None)
    pixel_values = df.iloc[0].values
    pixel_counts = df.iloc[1].values

    # 计算像素值的概率分布
    total_pixels = pixel_counts.sum()
    pixel_probabilities = pixel_counts / total_pixels

    # 计算信息熵
    entropy_value = entropy(pixel_probabilities, base=2)

    # 保存结果到同名txt文件中
    result_file_path = file_path.replace('.csv', '.txt')
    with open(result_file_path, 'w') as file:
        file.write(f'{entropy_value}')
    return entropy_value


def calculate_dct_entropy_not0(file_path):
    # 从CSV文件读取数据
    df = pd.read_csv(file_path, header=None)
    pixel_values = df.iloc[0].values
    pixel_counts = df.iloc[1].values

    non_zero_pixels = pixel_values[pixel_values != 0]
    non_zero_counts = pixel_counts[pixel_values != 0]
    # print(f'------------{non_zero_counts}--------------')
    # print(pixel_counts)
    # 计算像素值的概率分布
    total_pixels = non_zero_counts.sum()
    pixel_probabilities = non_zero_counts / total_pixels

    # 计算信息熵
    entropy_value = entropy(pixel_probabilities, base=2)

    # 保存结果到同名txt文件中
    result_file_path = file_path.replace('.csv', 'not0.txt')
    with open(result_file_path, 'w') as file:
        file.write(f'{entropy_value}')

    return entropy_value
# # 使用例子
# csv_file_path = 'your_csv_file.csv'  # 替换成实际的CSV文件路径
# entropy_value = calculate_entropy(csv_file_path)
# print(f'图像熵为: {entropy_value}')
