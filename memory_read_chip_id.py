import MT25QL01GBBB_20231023 as MT25QL01GBBB
import time

Flash = MT25QL01GBBB.flash()

try:
    while True:
        id_data = Flash.read_chip_id()
        print(f"読みだしたID: {id_data}")
        # 0ならOK
        # 
        
        # 1秒待機
        time.sleep(1)

except KeyboardInterrupt:
    print("\n監視を終了します。")

finally:
    # __del__が呼ばれるようにインスタンスを削除
    del Flash
    print("--- 監視終了 ---")