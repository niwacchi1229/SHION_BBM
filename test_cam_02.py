from picamera2 import Picamera2
import time
# 各カメラのインスタンスを作成（コンストラクタにインデックスを渡す）
# 引数を省略した場合、デフォルト（通常は0）のカメラが選択される
picam0 = Picamera2(0)
picam1 = Picamera2(1)

# それぞれのカメラを個別に設定・開始
# カメラ0の設定
# config0 = picam0.create_preview_configuration()でpreviewを使うとクロップされる。stillにするとフル画角で出てくるようになる
config0 = picam0.create_preview_configuration()
picam0.configure(config0)
picam0.start()

# カメラ1の設定
# カメラ0と同様
config1 = picam1.create_still_configuration()
picam1.configure(config1)
picam1.start()

# カメラの安定を待つ
time.sleep(2)

# それぞれのカメラで別々に撮影
picam0.capture_file("test_cam0_image_02.jpg")
picam1.capture_file("test_cam1_image_02.jpg")

print("finish")

# 後処理
picam0.stop()
picam1.stop()