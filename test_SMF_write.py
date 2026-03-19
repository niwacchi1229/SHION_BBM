import MT25QL01GBBB_20231023 as MT25QL01GBBB
import time
import spidev
from PIL import Image

# 設定項目
# 使用するメモリアドレス
TEST_ADDRESS = 0x00123400
# 書き込む画像
img = Image.open("test_input.jpg")

# Flashメモリのクラスをインスタンス化
Flash = MT25QL01GBBB.flash()

print("--- 外部フラッシュメモリの書き込み・読み出しテストを開始します ---")

try:
    #画像をバイナリデータに変換
    img = img.convert("RGB")
    with open("test_input.jpg" , "rb") as f :
        img_bin = f.read()
    write_data = list(img_bin)  # バイナリデータをリスト化しないとMT~~が動いてくれない
    file_size = len(write_data)
    print(f"ファイルサイズ: {file_size} バイト")
    print(write_data)

    # 1. 消去 (Erase)
    # ----------------------------------------------------------------
    # Flashメモリは、書き込む前に該当領域を消去する必要があります
    # ファイルサイズ分すべて消去
    print(f"1. アドレス {hex(TEST_ADDRESS)} から必要な範囲を消去")
    # 4KB単位で必要回数繰り替えす
    num_sectors = (file_size // 4096) + 1
    for i in range(num_sectors):
        addr = TEST_ADDRESS + (i * 4096)
        Flash.SUBSECTOR_4KB_ERASE_OF(addr)
    print("   -> 消去コマンドを送信しました。")
    # 消去処理には時間がかかるため、少し待機します。
    # (ライブラリ内でビジー状態をチェックしていますが、念のため)
    time.sleep(0.5) 
    print("   -> 消去完了。")
    
    # 書き込み - 256バイトずつに分割して書き込む
    print(f"\n2. アドレス {hex(TEST_ADDRESS)} にデータを書き込みます...")

    page_size = 256
    for i in range(0, file_size, page_size):
        # 256バイトずつ切り出す
        chunk = write_data[i : i + page_size]
        # アドレスをずらしながら書き込む
        Flash.WRITE_DATA_BYTES_SMF(TEST_ADDRESS + i, chunk)

        if (i // page_size) % 10 == 0:
            print(f"  -> 進捗: {i}/{file_size} bytes")    

    print("   -> 書き込み完了。")
    time.sleep(0.1)

    # 3. 読み出し (Read)
    # ----------------------------------------------------------------
    print(f"\n3. アドレス {hex(TEST_ADDRESS)} からデータを読み出します...")
    
    print("   -> READ_DATA_BYTES_SMF関数を呼び出します...")
    # 書き込んだデータと同じ長さを読み出します。
    read_data_bytes = Flash.READ_DATA_BYTES_SMF(TEST_ADDRESS, len(write_data))
    print("   -> READ_DATA_BYTES_SMF関数から戻りました。")
    print(f"   -> 読み出した生のバイトデータ: {read_data_bytes}") # 取得した生データを表示
    
    # 読み出したバイトリストを文字列に変換します。
    read_string = ""
    if read_data_bytes:
        try:
            print("   -> バイトデータをUTF-8文字列にデコードします...")
            read_string = bytes(read_data_bytes).decode('utf-8')
            print("   -> デコード成功。")
        except UnicodeDecodeError:
            read_string = "（デコード不可能なバイナリデータ）"
            print("   -> デコード失敗。")

    print(f"   -> 読み出したデータ: '{read_string}'")
    print("   -> 読み出し完了。")
    
    # 4. 検証 (Verify)
    # ----------------------------------------------------------------
    print("\n4. データの検証を行います...")
    if img == read_string:
        print("   ✅ [成功] 書き込んだデータと読み出したデータが完全に一致しました！")
    else:
        print("   ❌ [失敗] データが一致しませんでした。")

except Exception as e:
    print(f"\nエラーが発生しました: {e}")
    print("SPIの接続や権限などを確認してください。")

finally:
    print("\n--- テストを終了します ---")