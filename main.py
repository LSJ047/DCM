from utils.cdm_info import get_dcms_info
from utils.dcm2csv import convert_dcm_to_csv
from utils.divide import divide_3, divide_2
from utils.dct import dct
from utils.statistics import statistics, statistics_dct
from utils.spliet_channels import split_channels
from utils.entropy_value import calculate_entropy, calculate_entropy_not0, calculate_dct_entropy_not0, calculate_dct_entropy
from utils.dcm2png import dcm_to_png, png_to_csv
from utils.csv2png import csv_to_png
from utils.rgb2yuv import RGB2YUV

import os

# dcm文件夹路径
dcm_directory = r'E:/study/pythonProject/DCM/data/dcm'
results = r'E:/study/pythonProject/DCM/results'

# # 获取dcm数据集的具体信息（图像的W,H,size等）
# get_dcms_info(dcm_directory)
# 将dcm文件转换成csv格式
# convert_dcm_to_csv(dcm_directory + '/1-26.dcm')

###################csv2png#############
# dcm_to_png(dcm_directory + '/1-26.dcm', 'E:/study/pythonProject/DCM/data/png/1-26.png')


# ###########查看通道##############
# from PIL import Image
#
# def get_image_info(image_path):
#     try:
#         # 打开图像
#         with Image.open(image_path) as img:
#             # 获取图像格式和通道数
#             format = img.format
#             mode = img.mode
#
#             return format, mode
#     except Exception as e:
#         return None, None
#
# # 使用例子
# image_path = 'E:/study/pythonProject/DCM/data/png/1-26.png'  # 替换成实际的图像文件路径
# format, mode = get_image_info(image_path)

# if format and mode:
#     print(f'图像格式: {format}')
#     print(f'通道模式: {mode}')
# else:
#     print('无法获取图像信息')
#

ls = []


def main():
    dcm_directory: str = r'E:/study/pythonProject/DCM/data/dcm'
    results = r'E:/study/pythonProject/DCM/results'

    Name = '/1-26'
    DIR1 = results + Name
    #########截断##############
    # divide_2(DIR1 + '/8_LSB.csv', DIR1, 5)
    divide_3(DIR1 + '/8_LSB.csv', DIR1, 2, 3, 3)
    divide_3(DIR1 + '/8_LSB.csv', DIR1, 3, 2, 3)
    divide_3(DIR1 + '/8_LSB.csv', DIR1, 3, 3, 2)
    ################统计分布################
    statistics(DIR1 + '/8_LSB')

    ############计算熵###########
    DIR2 = DIR1 + '/8_LSB_statistics'
    for root, dirs, files in os.walk(DIR2):
        for file in files:
            if file.endswith('.csv'):
                if os.path.join(root, file).startswith(DIR2):
                    entropy_value = calculate_entropy(os.path.join(DIR2, file))
                    entropy_value_not0 = calculate_entropy_not0(os.path.join(DIR2, file))
                    print(f'{file}图像熵为: {entropy_value}')
                    print(f'{file}图像熵(去0)为: {entropy_value_not0}')


def main2():
    dcm_directory: str = r'E:/study/pythonProject/DCM/data/dcm'
    results = r'E:/study/pythonProject/DCM/results'

    Name = '/1-26'
    DIR1 = results
    #########截断##############
    divide_2(dcm_directory + '/1-26.csv', DIR1, 8)
    divide_3(dcm_directory + '/1-26.csv', DIR1, 8, 4, 4)
    divide_3(dcm_directory + '/1-26.csv', DIR1, 8, 2, 6)
    divide_3(dcm_directory + '/1-26.csv', DIR1, 8, 6, 2)
    divide_3(dcm_directory + '/1-26.csv', DIR1, 8, 3, 5)
    divide_3(dcm_directory + '/1-26.csv', DIR1, 8, 5, 3)
    ################统计分布################
    statistics(DIR1 + Name)

    ############计算熵###########
    DIR2 = DIR1 + Name + '_statistics'
    for root, dirs, files in os.walk(DIR2):
        for file in files:
            if file.endswith('.csv'):
                if os.path.join(root, file).startswith(DIR2):
                    entropy_value = calculate_entropy(os.path.join(DIR2, file))
                    entropy_value_not0 = calculate_entropy_not0(os.path.join(DIR2, file))
                    print(f'{file}图像熵为: {entropy_value}')
                    print(f'{file}图像熵(去0)为: {entropy_value_not0}')


# if __name__ == '__main__':
    # main()
    # main2()

# dct('E:/study/pythonProject/DCM/results/1-26')
# statistics_dct(results + '/1-26_dct')
# dct('E:/study/pythonProject/DCM/results/1-26/8_LSB')
# statistics(results + '/1-26/8_LSB_dct')
# DIR2 = 'E:/study/pythonProject/DCM/results/1-26_dct_statistics'
# for root, dirs, files in os.walk(DIR2):
#     for file in files:
#         if file.endswith('.csv'):
#             if os.path.join(root, file).startswith(DIR2):
#                 entropy_value = calculate_dct_entropy(os.path.join(DIR2, file))
#                 entropy_value_not0 = calculate_dct_entropy_not0(os.path.join(DIR2, file))
#                 print(f'{file}图像熵为: {entropy_value}')
#                 print(f'{file}图像熵(去0)为: {entropy_value_not0}')


def c2p(P, N):
    for file in os.listdir(P):
        if file.endswith('.csv'):
            try:
                input_path = os.path.join(P, file)
                output_path = os.path.join(P, file[:-4] + N)
                csv_to_png(input_path, output_path)
            except Exception as e:
                print(f"Error processing {file}: {e}")
                continue


# P = r'E:/study/pythonProject/DCM/results/1-26/8_LSB'
# P = r'E:/study/pythonProject/DCM/results/1-26'
# P = dcm_directory
# N = '.png'
# c2p(P, N)
# csv_to_png('/results/outputs/output_gray_y_422-2.csv', 'E:/study/pythonProject/DCM/data/dcm/output_gray_y_422-2.png')


png_to_csv(results+'/outputs/single_channels_low_output1.png', results+'/outputs/single_channels_low_output1.csv')
png_to_csv(results+'/outputs/single_channels_low_output2.png', results+'/outputs/single_channels_low_output2.csv')
png_to_csv(results+'/outputs/single_channels_low_output3.png', results+'/outputs/single_channels_low_output3.csv')
statistics(results + '/outputs')
calculate_entropy(results + '/outputs_statistics/static_single_channels_low_output1.csv')
calculate_entropy(results + '/outputs_statistics/static_single_channels_low_output2.csv')
calculate_entropy(results + '/outputs_statistics/static_single_channels_low_output3.csv')
