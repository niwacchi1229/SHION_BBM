import cv2

# 画像を開く
img = cv2.imread('input.dng')



if img is None:
    print("画像ファイルが見つからないか、読み込めていない")
else:
    # 設定項目
    campression_pith = 15
    quality = 10

    # リサイズ
    img_resized = cv2,resize(img, new_size, interpolation=cv2.INTER_AREA)
    