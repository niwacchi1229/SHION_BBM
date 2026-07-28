from gpiozero import OutputDevice
import time

# プログラム上では「物理ピン24番」＝「GPIO 8」として指定します
TARGET_GPIO = 8

# GPIO 8を出力用のピン（電気を送り出す側）として設定します
pin24 = OutputDevice(TARGET_GPIO)

try:
    print("24番ピン（GPIO 8）をオン(HIGH)にします！")
    # ピンに電気を流します（3.3V）
    pin24.on()
    
    # オンの状態のまま3秒間待機します
    time.sleep(5)
    
    print("24番ピン（GPIO 8）をオフ(LOW)にします！")
    # ピンの電気を止めます（0V）
    pin24.off()

except KeyboardInterrupt:
    # ユーザーが「Ctrl + C」を押して強制終了した際の安全策です
    print("\nプログラムを中断し、ピンを安全な状態に戻します。")
finally:
    # プログラム終了時は必ずオフにして安全を確保します
    pin24.off()