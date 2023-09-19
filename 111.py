# import csv
# import numpy as np
#
# # 读取原始 CSV 文件
# original_csv_file = 'E:/study/pythonProject/DCM/results/outputs/output_gray_y_422-2.csv'  # 替换成你的原始 CSV 文件路径
# output_csv_file = 'E:/study/pythonProject/DCM/results/outputs/output.csv'    # 替换成你的输出 CSV 文件路径
#
# # 从原始 CSV 文件读取数据
# data = []
# with open(original_csv_file, 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         data.append(row[0])  # 假设原始文件只有一列数
# # 确保数据数量足够填充到目标大小
# if len(data) < 700 * 460:
#     raise ValueError("数据数量不足以填充到目标大小")
#
# # 将数据重新排列成 700x460 大小的数组
# reshaped_data = np.reshape(data[:700 * 460], (700, 460))
#
# # 将重新排列的数据写入到输出 CSV 文件
# with open(output_csv_file, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for row in reshaped_data:
#         writer.writerow(row)
#
# print(f"已生成 {output_csv_file}")
#
#
