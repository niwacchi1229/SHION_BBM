from picamera2 import Picamera2

# カメラオブジェクトの作成
picam2 = Picamera2()

# カメラを開始、１枚撮影して保存する
# デフォルトの場合、１秒の待機後に"test.jpg"の名前で保存
picam2.start_and_capture_file("test.jpg")