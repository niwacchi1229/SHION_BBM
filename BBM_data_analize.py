import MT25QL01GBBB_20231023 as MT25QL01GBBB
import os

Flash = MT25QL01GBBB.flash()

# ---設定---
start_address = 0x03761000    # 03761000 # 書き込み開始アドレス
SAVE_FILE_NAME = "restored_image.jpg"
# 書き込んだ画像の正確なファイルサイズが必要(バイト)
data_size = 1645
# spi通信で一度に4096bytes以上送受信するとエラーが起こるため切り分けて行う
CHUNK_SIZE = 2048
# 1667762
all_data = bytearray()

print(f"--- アドレス {hex(start_address)} から画像復元開始---")

try:
    for i in range(start_address, start_address + data_size, CHUNK_SIZE):
        # SMFからデータを取得
        data = Flash.READ_DATA_BYTES_SMF(i, CHUNK_SIZE)
        all_data.extend(data)

    print(f"ファイル '{SAVE_FILE_NAME}' に保存します")
    with open(SAVE_FILE_NAME, "wb") as f:
        f.write(bytes(all_data))
    
    print(bytes(all_data))

        # if (len(all_data) % (CHUNK_SIZE * 50)) == 0:
        #     print(f"現在: {len(all_data) / }")

    # 1.　フラッシュメモリからデータを読み出し
    # READ_DATA_BYTES_SMFは　0x13　コマンド（4バイトアドレス読み込み
    # print(f"読み出し中 （サイズ: {data_size} バイト")
    # read_data = Flash.READ_DATA_BYTES_SMF(TEST_ADDRESS, IMAGE_SIZE)

    # 読みだしたデータをバイナリファイルとして保存
    # 取得されるデータはリスト形式なのでbytes()で変換して書き込む
    # print(f"ファイル '{SAVE_FILE_NAME}' に保存します")
    # with open(SAVE_FILE_NAME, "wb") as f:
    #     f.write(bytes(read_data))
    
    

    print("復元完了")

    print("バイナリデータの読み込み開始")
    with open(SAVE_FILE_NAME , "rb") as f :
        img_bin = f.read()
    print(f"---バイナリデータの表示---\n{img_bin}")

except Exception as e:
    print(f"\nエラーが発生しました: {e}")
    print("SPIの接続や権限などを確認してください。")

finally:
    print("\n--- テストを終了します ---")