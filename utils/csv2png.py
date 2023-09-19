from PIL import Image
import csv
import numpy as np


def csv_to_png(csv_file_path, output_png_path):
    # 从CSV文件读取数据
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        matrix = list(reader)

    # 转换成NumPy数组
    matrix = np.array(matrix, dtype=np.uint16)
    # 创建单通道的灰度图像
    image = Image.fromarray(matrix, mode='I;16')

    # 保存为PNG图片
    image.save(output_png_path)

# # 使用例子
# csv_file_path = 'input.csv'  # 替换成实际的CSV文件路径
# output_png_path = 'output.png'  # 替换成输出PNG文件路径
#
# csv_to_png(csv_file_path, output_png_path)
