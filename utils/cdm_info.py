import pydicom
import os
import csv


def get_image_info(dicom_path):
    ds = pydicom.dcmread(dicom_path)
    return {
        'Name': ds.SOPInstanceUID,
        'File Name': dicom_path,
        'Width': ds.Columns,
        'Height': ds.Rows,
        'Bit Depth': ds.BitsStored,
        'Size (bytes)': os.path.getsize(dicom_path),
        'Format': ds.SOPClassUID.name
    }


def count_bit_depths_dicom(directory):
    bit_depth_info = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.dcm'):
                dicom_path = os.path.join(root, file)
                image_info = get_image_info(dicom_path)
                bit_depth_info.append(image_info)
    return bit_depth_info


def get_dcms_info(directory):

    bit_depth_info = count_bit_depths_dicom(directory)

    csv_file = os.path.join(directory, 'images_info.csv')
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Name', 'File Name', 'Width', 'Height', 'Bit Depth', 'Size (bytes)', 'Format']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for info in bit_depth_info:
            writer.writerow(info)

    print(f'信息已写入到 {csv_file}')


# get_dcms_info(r'E:/study/pythonProject/DCM/data/dcm/')