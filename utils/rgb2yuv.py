import numpy as np
import cv2
import pandas as pd


def YUV2RGB(img):
    img = img.astype(np.float32)

    y, u, v = np.split(img, 3, axis=2)

    g = y - np.round((86 * v + 29 * u) / 256.0)
    r = v + g
    b = u + np.round((87 * r + 169 * g) / 256.0)

    rgb_img = np.concatenate([r, g, b], axis=2)

    return (rgb_img).astype(np.uint8)


def RGB2YUV(imgpath, output):
    img = cv2.cvtColor(cv2.imread(imgpath), cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32)

    r, g, b = np.split(img, 3, axis=2)

    u = b - np.round((87 * r + 169 * g) / 256.0)
    v = r - g
    y = g + np.round((86 * v + 29 * u) / 256.0)

    yuv_img = np.concatenate([y, u, v], axis=2)

    # 将Y、U、V三个通道的值分别保存到CSV文件
    yuv_channels = ['Y', 'U', 'V']
    for i, channel in enumerate(yuv_channels):
        channel_data = yuv_img[:, :, i]
        channel_csv_file = f'{output}{channel}.csv'
        df = pd.DataFrame(channel_data)
        df.to_csv(channel_csv_file, index=False, header=False)
        print(f'{channel} 通道数据已保存到 {channel_csv_file}')



