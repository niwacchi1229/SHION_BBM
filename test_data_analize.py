import MT25QL01GBBB_20231023 as MT25QL01GBBB
import os

# ---設定---
TEST_ADDRESS = 0x03761000 # 書き込み開始アドレス
SAVE_FILE_NAME = "restored_image.jpg"
# 書き込んだ画像の正確なファイルサイズが必要(バイト)
IMAGE_SIZE = 1845351
# spi通信で一度に4096bytes以上送受信するとエラーが起こるため切り分けて行う
# 実際にはPacket内に [0x00] * amountが含まれるため、より小さい値が必要
CHUNK_SIZE = 2048
# 1667762
Flash = MT25QL01GBBB.flash()

print(f"--- アドレス {hex(TEST_ADDRESS)} から画像復元開始---")

try:
    # 1.　フラッシュメモリからデータを読み出し
    # READ_DATA_BYTES_SMFは　0x13　コマンド（4バイトアドレス読み込み
    print(f"読み出し中 (サイズ: {IMAGE_SIZE} バイト)")
    
    # チャンク単位で分割読み込み（SPI通信は4096バイト制限）
    read_data = []
    for offset in range(0, IMAGE_SIZE, CHUNK_SIZE):
        chunk_size = min(CHUNK_SIZE, IMAGE_SIZE - offset)
        current_address = TEST_ADDRESS + offset
        print(f"  {offset}/{IMAGE_SIZE} バイト読み込み中...", end='\r')
        chunk = Flash.READ_DATA_BYTES_SMF(current_address, chunk_size)
        read_data.extend(chunk)
    print(f"読み出し完了: {IMAGE_SIZE} バイト")  # 改行して完了表示

    # 読みだしたデータをバイナリファイルとして保存
    # 取得されるデータはリスト形式なのでbytes()で変換して書き込む
    print(f"ファイル '{SAVE_FILE_NAME}' に保存します")
    with open(SAVE_FILE_NAME, "wb") as f:
        f.write(bytes(read_data))
    
    

    print("復元完了")

    print("バイナリデータの読み込み開始")
    with open(SAVE_FILE_NAME , "rb") as f :
        img_bin = f.read()
    print(f"ファイルサイズ: {len(img_bin)} バイト")

except Exception as e:
    print(f"\nエラーが発生しました: {e}")
    print("SPIの接続や権限などを確認してください。")

finally:
    print("\n--- テストを終了します ---")