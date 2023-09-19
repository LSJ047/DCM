import cv2
import numpy as np
import openpyxl
import pandas as pd
import os


def dct_transform(component):
    component = component.to_numpy()
    block_size = 8
    # block_size = 4
    height, width = component.shape
    dct_coeffs = np.zeros_like(component, dtype=np.float32)

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = component[y:y + block_size, x:x + block_size].astype(np.float32)
            dct_block = cv2.dct(block)
            dct_coeffs[y:y + block_size, x:x + block_size] = dct_block

    return dct_coeffs.astype(int)


def dct(input_dir):
    output_dct_dir = os.path.join(os.path.dirname(input_dir), input_dir + '_dct/')
    if not os.path.exists(output_dct_dir):
        os.mkdir(output_dct_dir)
    for file in os.listdir(input_dir):
        if file.endswith('.csv'):
            input_csv = pd.read_csv(os.path.join(input_dir, file))
            # 对每个元素进行DCT变换
            dct_transformed = dct_transform(input_csv)
            # 将变换后的结果保存为CSV文件
            dct_df = pd.DataFrame(dct_transformed)
            new_file_name = os.path.join(output_dct_dir, file[: -4] + '_dct.csv') # 新文件名
            dct_df.to_csv(new_file_name, index=False, header=False)
