import MT25QL01GBBB_20231023 as MT25QL01GBBB
import os

# ---設定---
TEST_ADDRESS = 0x00123400 # 書き込み開始アドレス
SAVE_FILE_NAME = "restored_image.jpg"
# 書き込んだ画像の正確なファイルサイズが必要(バイト)
IMAGE_SIZE = 1312

Flash = MT25QL01GBBB.flash()

print(f"--- アドレス {hex(TEST_ADDRESS)} から画像復元開始---")

try:
    # 1.　フラッシュメモリからデータを読み出し
    # READ_DATA_BYTES_SMFは　0x13　コマンド（4バイトアドレス読み込み
    print(f"読み出し中 （サイズ: {IMAGE_SIZE} バイト")
    read_data = Flash.READ_DATA_BYTES_SMF(TEST_ADDRESS, IMAGE_SIZE)

    # 読みだしたデータをバイナリファイルとして保存
    # 取得されるデータはリスト形式なのでbytes()で変換して書き込む
    print(f"ファイル '{SAVE_FILE_NAME}' に保存します")
    with open(SAVE_FILE_NAME, "wb") as f:
        f.write(bytes(read_data))

    print("復元完了")

except Exception as e:
    print(f"\nエラーが発生しました: {e}")
    print("SPIの接続や権限などを確認してください。")

finally:
    print("\n--- テストを終了します ---")