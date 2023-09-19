from PIL import Image
import numpy as np
import pandas as pd
import os


def split_channels(image_path, output_folder):
    # 打开图像
    with Image.open(image_path) as img:
        # 将图像转换成NumPy数组
        img_array = np.array(img)

        # 分割通道
        red_channel = img_array[:, :, 0]
        green_channel = img_array[:, :, 1]
        blue_channel = img_array[:, :, 2]

        # 保存通道数据到CSV文件
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        pd.DataFrame(red_channel).to_csv(f'{output_folder}/red_channel.csv', index=False, header=False)
        pd.DataFrame(green_channel).to_csv(f'{output_folder}/green_channel.csv', index=False, header=False)
        pd.DataFrame(blue_channel).to_csv(f'{output_folder}/blue_channel.csv', index=False, header=False)

# # 使用例子
# image_path = 'example.jpg'  # 替换成实际的图像文件路径
# output_folder = 'output'  # 存放CSV文件的文件夹，确保该文件夹已存在
# split_channels(image_path, output_folder)
