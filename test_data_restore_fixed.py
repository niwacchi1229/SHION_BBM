import MT25QL01GBBB_20231023 as MT25QL01GBBB

# ---設定---
TEST_ADDRESS = 0x03761000 # 書き込み開始アドレス
SAVE_FILE_NAME = "restored_image_fixed.jpg"
IMAGE_SIZE = 1845351
CHUNK_SIZE = 2048

Flash = MT25QL01GBBB.flash()

print(f"--- アドレス {hex(TEST_ADDRESS)} から画像復元開始（修正版）---")

try:
    # チャンク単位で分割読み込み
    read_data = []
    for offset in range(0, IMAGE_SIZE, CHUNK_SIZE):
        chunk_size = min(CHUNK_SIZE, IMAGE_SIZE - offset)
        current_address = TEST_ADDRESS + offset
        print(f"  {offset}/{IMAGE_SIZE} バイト読み込み中...", end='\r')
        chunk = Flash.READ_DATA_BYTES_SMF(current_address, chunk_size)
        read_data.extend(chunk)
    
    print(f"読み出し完了: {IMAGE_SIZE} バイト")
    
    # 読みだしたデータをバイナリファイルとして保存
    print(f"ファイル '{SAVE_FILE_NAME}' に保存します")
    with open(SAVE_FILE_NAME, "wb") as f:
        f.write(bytes(read_data))
    
    print("復元完了")
    
    # 先頭バイトの確認
    print(f"\n先頭32バイト（16進数）: {' '.join(f'{b:02x}' for b in read_data[:32])}")
    
    # JPEGマジックナンバーの検索
    target = bytes([0xd8, 0xff])
    jpeg_pos = bytes(read_data).find(target)
    if jpeg_pos != -1:
        print(f"\nJPEGマジックナンバー (D8 FF) が位置 {hex(jpeg_pos)} にあります")
        print(f"オフセット: {jpeg_pos} バイト")
        if jpeg_pos > 0:
            print("\n※ ファイルの先頭に不要なデータがあります")
            print(f"正しいJPEGは位置 {jpeg_pos} から始まります")

except Exception as e:
    print(f"\nエラーが発生しました: {e}")
    print("SPIの接続や権限などを確認してください。")

finally:
    print("\n--- テストを終了します ---")
