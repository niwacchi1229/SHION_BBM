import cv2
import numpy as np
import rawpy

print("WebPへの現像を開始します")

try:
    # 設定項目
    # WEBPのクオリティは0~100で指定する(低いほど高圧縮)
    quality = 100
    # リサイズ(各辺を何分の1にするか)
    compression_pith = 2

    # 読み込む画像ファイル
    input_path = 'input.dng'
    # 出力されるファイル名
    output_path = f"img_resized_Q{quality}_C{compression_pith}.webp"

    # rawpyでDNGを開く
    with rawpy.imread(input_path) as raw:
        # 現像処理
        # use_camera_wb=True : カメラの設定通りの色にする
        # no_auto_bright=False : 明るさを自動調節する
        rgb = raw.postprocess(use_camera_wb=True, no_auto_bright=False, bright=1.0)

    # OpenCVで扱えるように色を変換
    img = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    # リサイズ
    new_width = img.shape[1] // compression_pith
    new_height = img.shape[0] // compression_pith
    new_size = (new_width, new_height)

    img_resized = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

    # WebP形式で保存
    params = [int(cv2.IMWRITE_WEBP_QUALITY), quality]

    # ファイル名
    cv2.imwrite(output_path, img_resized, params)

    print(f"圧縮完了 サイズ: {new_height}✕{new_width}")

except Exception as e:
    print(f"\nエラーが発生しました: {e}")

finally:
    print("\n--- 終了します ---")


    