from gpiozero import LED
from time import sleep
import signal
import sys

# 制御したいGPIOピン番号を指定（ここでは17番）
# gpiozeroでは「LED」クラスをデジタル出力デバイスとして流用するのが簡単です
dio_pin = LED(25)

print("--- DIO Signal Toggler Start ---")
print("Target Pin: GPIO 17")
print("Interval  : 10 Seconds")
print("Press Ctrl+C to stop.")

def signal_handler(sig, frame):
    print("\nStopping...")
    dio_pin.off() # 終了時はLowにして安全に閉じる
    sys.exit(0)

# Ctrl+Cで綺麗に終了するための設定
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        # Highにする
        print("Signal: HIGH (3.3V)")
        dio_pin.on()
        sleep(5)

        # Lowにする
        print("Signal: LOW (0V)")
        dio_pin.off()
        sleep(5)

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    dio_pin.off()