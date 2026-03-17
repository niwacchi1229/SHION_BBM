from picamera2 import Picamera2
import time
import os

# パラメーターの設定
# シャッタースピード：1s = 1,000,000
SHUTTER_SPEED = 100000
# ISOの設定：1.0(ISO100),2.0(ISO200)
ISO_GAIN = 4.0

# カメラのインスタンスを作成（コンストラクタにインデックスを渡す）
# 引数を省略した場合、デフォルト（通常は0）のカメラが選択される
picam0 = Picamera2(0)

# マニュアル設定を適用
# 露光時間、ゲインを固定する
picam0.set_controls({"ExposureTime": SHUTTER_SPEED, "AnalogueGain": ISO_GAIN})

# カメラの設定、開始
# config0 = picam0.create_preview_configuration()でpreviewを使うとクロップされる。stillにするとフル画角で出てくるようになる
config0 = picam0.create_still_configuration(raw={})
picam0.configure(config0)
picam0.start()

# カメラを安定させるための時間
time.sleep(0.5)

print("撮影開始")

# 撮影の基準時間
start_time = time.time()

try:
    for i in range(1, 23): # 1~22まで繰り返す
        # 次の撮影予定時間
        target_time = start_time + (i - 1)

        # 予定の時間まで待機
        wait_time = target_time - time.time()
        if wait_time > 0:
            time.sleep(wait_time)

        print(wait_time)
        
        # ファイル名
        file0 = f"raw_SS100000_ISO4_{i:02d}.dng"

        # 撮影
        picam0.capture_file(file0, "raw")

        print(f"{i}/22 枚")

except KeyboardInterrupt:
    print("\n中断されました")
        
finally:
    # 後処理
    picam0.stop()
    print("all finish")