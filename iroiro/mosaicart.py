import os

import cv2
import numpy as np

# 平均明度を計算する。入力：ndarray型, 出力：int型
def average_brightness(img):
    return int(img.mean())

# 平均彩度を計算する。入力：ndarray型, 出力：int型 × 3
def average_saturation(img):
    r = int(img[:, :, 0].mean())
    g = int(img[:, :, 1].mean())
    b = int(img[:, :, 2].mean())
    return r, g, b

# 元画像とサブ画像を対応付けて、サブ画像の並び順を決定する。
# 入力：list型 × 2, 出力：list型
def decide_order(a_elements, b_elements):
    junban = []
    for a_element in a_elements:
        scores = [abs(sum(a_element - b_element)) for b_element in b_elements]
        for i in range(len(scores)):
            if scores[i] == min(scores):
                junban += [i]
                break
    return junban

# メイン関数
def main(motogazo, x_bunkatsu, y_bunkatsu, sub_image_dir,
         result_filename, x_size_result, y_size_result):
    # 元画像を読み込む
    img = cv2.imread(motogazo)
    
    # サブ画像のサイズを計算する
    x_size = int(img.shape[0]/x_bunkatsu)
    y_size = int(img.shape[1]/y_bunkatsu)
    
    # 元画像の明度、彩度を計算してListに格納する。
    img_elements = []
    for y in range(y_bunkatsu):
        for x in range(x_bunkatsu):
            tmp = img[x*x_size:(x+1)*x_size, y*y_size:(y+1)*y_size]
            brightness = average_brightness(tmp)
            r, g, b = average_saturation(tmp)
            img_elements.append(np.array([brightness, r, g, b]))

    print("Mozaiku art image size: {}".format(len(img_elements)))

    # サブ画像のパスを求める。
    file_pathes = [os.path.join(sub_image_dir, i) for i in os.listdir(sub_image_dir)]
    
    print("Sub image number: {}".format(len(file_pathes)))
    
    # サブ画像の明度・彩度を計算したListに格納する。
    sub_img_elements = []
    for i in range(len(file_pathes)):
        img = cv2.imread(file_pathes[i])
        
        brightness = average_brightness(img)
        r, g, b = average_saturation(img)
        sub_img_elements.append(np.array([brightness, r, g, b]))

    # 元画像とサブ画像の明度・彩度を比較して、サブ画像の並び順を決定する。
    junban = decide_order(img_elements, sub_img_elements)

    # モザイクアートの下地を生成する。
    img_result = np.zeros((x_size_result, y_size_result, 3), dtype=np.uint8)

    x_size = int(x_size_result/x_bunkatsu)
    y_size = int(y_size_result/y_bunkatsu)

    # junban に入っているサブ画像の順番の通り画像を並べていきます。
    for y in range(y_bunkatsu):
        for x in range(x_bunkatsu):
            img = cv2.imread(file_pathes[junban[x+x_bunkatsu*y]])
            img = cv2.resize(img, (x_size, y_size))
            img_result[x*x_size:(x+1)*x_size, y*y_size:(y+1)*y_size] = img

    cv2.imwrite(result_filename, img_result)


if __name__ == "__main__":
    """
        CONSTRAINTS:
        1.motogazo size is the multiple of x_bunkatsu and y_bunkatsu
        2.x(y)_size_result is the multiple of x(y)_bunkatsu
        """
    # 入力画像の情報
    motogazo = "ban_2.jpg"
    x_bunkatsu = 64
    y_bunkatsu = 64
    sub_image_dir = "ban_img"
    
    # 出力画像の情報
    result_filename = "ban_2_mosaicart.bmp"
    x_size_result = 2048
    y_size_result = 2048
    
    main(motogazo, x_bunkatsu, y_bunkatsu, sub_image_dir,
         result_filename, x_size_result, y_size_result)
