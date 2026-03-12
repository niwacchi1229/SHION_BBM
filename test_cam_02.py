from picamera2 import Picamera2
import time
import os

# 保存用ディレクトリの作成
os.makedirs("testcaptures", exist_ok=True)

# 各カメラのインスタンスを作成（コンストラクタにインデックスを渡す）
# 引数を省略した場合、デフォルト（通常は0）のカメラが選択される
picam0 = Picamera2(0)
# picam1 = Picamera2(1)

# それぞれのカメラを個別に設定・開始
# カメラ0の設定
# config0 = picam0.create_preview_configuration()でpreviewを使うとクロップされる。stillにするとフル画角で出てくるようになる
config0 = picam0.create_still_configuration()
picam0.configure(config0)
picam0.start()

# カメラ1の設定
# カメラ0と同様
# config1 = picam1.create_still_configuration()
# picam1.configure(config1)
# picam1.start()

# カメラを安定させるための時間
time.sleep(1)

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
        file0 = f"image_cam0_{i:02d}.jpg"
        # file1 = f"image_cam1_{i:02d}.jpg"

        # 撮影
        picam0.capture_file(file0)
        # picam1.capture_file(file1)

        print(f"{i}/22 枚")

except KeyboardInterrupt:
    print("\n中断されました")
        
finally:
    # 後処理
    picam0.stop()
    # picam1.stop()
    print("all finish")