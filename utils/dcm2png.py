import pydicom
from PIL import Image
import numpy as np
import pandas as pd


def png_to_csv(png_path, csv_path):
    # 读取PNG图像
    image = Image.open(png_path)

    # 将图像数据转换为NumPy数组
    pixel_data = np.array(image)

    # 创建DataFrame
    df = pd.DataFrame(pixel_data)

    # 将DataFrame保存为CSV文件
    df.to_csv(csv_path, index=False, header=False)


def dcm_to_png(dcm_path, png_path):
    # 读取DICOM文件
    dcm_data = pydicom.dcmread(dcm_path)

    # 获取高宽对应的数据
    pixel_data = dcm_data.pixel_array

    # 保存为PNG图片
    image = Image.fromarray(pixel_data, mode='I;16')
    image.save(png_path)
    png_to_csv(png_path, png_path[:-4] + '_.csv')

# # 使用例子
# dcm_file_path = 'input.dcm'  # 替换成实际的DICOM文件路径
# output_png_path = 'output.png'  # 替换成输出PNG文件路径
#
# dcm_to_png(dcm_file_path, output_png_path)
