import cv2
import time

# 画像を開く
img = cv2.imread('input.dng')

try:
    # リサイズ
    compression_pith = 2
    new_width = img.shape[1] // compression_pith
    new_height = img.shape[0] // compression_pith
    new_size = (new_width, new_height)

    img_resized = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

    # Jpeg形式で保存
    # JPEGのクオリティは0~100で指定する
    quality = 100
    params = [int(cv2.IMWRITE_JPEG_QUALITY), quality]

    # ファイル名
    file_name = f"image_resize_{i:02d}.jpg"
    cv2.imwrite(file_name, img_resized, params)

    print(f"圧縮完了　サイズ: {new_height}✕{new_width}")

except Exception as e:
    print(f"\nエラーが発生しました: {e}")

finally:
    print("\n--- 終了します ---")



#if img is None:
#    print("画像ファイルが見つからないか、読み込めていない")
#else:
    # 設定項目
#    campression_pith = 15
#    quality = 10

    # リサイズ
#    img_resized = cv2,resize(img, new_size, interpolation=cv2.INTER_AREA)
    