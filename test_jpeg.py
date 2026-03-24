import cv2
import numpy as np
import rawpy

# 読み込む画像ファイル
input_path = 'input.dng'
output_path = 'genzou_01.jpg'

try:
    # rawpyでDNGを開く
    with rawpy.imread(input_path) as raw:
        # 現像処理
        # use_camera_wb=True : カメラの設定通りの色にする
        # no_auto_bright=False : 明るさを自動調節する
        rgb = raw.postprocess(use_camera_wb=True, no_auto_bright=False, bright=1.0)

    # OpenCVで扱えるように色を変換
    img = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

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
    file_name = f"image_resized.jpg"
    cv2.imwrite(file_name, img_resized, params)

    print(f"圧縮完了 サイズ: {new_height}✕{new_width}")

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
    