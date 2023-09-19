import pydicom
import pandas as pd
import os


def convert_dcm_to_csv(dcm_path):
    csv_path = dcm_path[: -4] + '.csv'
    # 读取DICOM文件
    dcm_data = pydicom.dcmread(dcm_path)

    # 获取高宽对应的数据
    pixel_data = dcm_data.pixel_array

    # 将pixel_data转换成DataFrame
    df = pd.DataFrame(pixel_data)

    # 将DataFrame写入CSV文件
    df.to_csv(csv_path, index=False, header=False)
    print(f'{dcm_path} 经 转 换 为 {csv_path}')

# 指定输入的DICOM文件和输出的CSV文件路径
# dcm_file_path = r'E:/study/pythonProject/DCM/data/dcm/'
# csv_file_path = './csv-4/1-26.csv'
#
# # 调用函数进行转换
# convert_dcm_to_csv(dcm_file_path, csv_file_path)
